def read():
    return list(map(int, input().split()))


(n, k) = read()
a = []
w = 0
q = []
for i in range(n):
    q.append(w)
b = []
for i in range(n):
    b.append(q.copy())
for i in range(n):
    a.append(input())
"if k==1:\n    ans=0\n    for i in range(n):\n        for j in range(n):\n            if a[i][j]=='.':\n                ans+=1\n    print(ans)\n    return"
for i in range(n):
    for j in range(n - k + 1):
        for l in range(j, j + k):
            if a[i][l] == '#':
                break
        else:
            for l in range(j, j + k):
                b[i][l] += 1
for i in range(n):
    for j in range(n - k + 1):
        for l in range(j, j + k):
            if a[l][i] == '#':
                break
        else:
            for l in range(j, j + k):
                b[l][i] += 1
m = 0
ai = 1
aj = 1
for i in range(n):
    for j in range(n):
        if b[i][j] > m:
            m = b[i][j]
            ai = i + 1
            aj = j + 1
print(ai, aj)
