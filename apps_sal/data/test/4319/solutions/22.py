n = int(input())
m = list(map(int, input().split()))
s = 0
q = []
w = 1
for i in range(1, n):
    if m[i] == m[i - 1] + 1:
        w += 1
    else:
        q.append(w)
        s += 1
        w = 1
q.append(w)
s += 1
print(s)
for i in range(len(q)):
    print(q[i], end=' ')
