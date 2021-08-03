n, m = list(map(int, input().split()))
ma = []
for i in range(n):
    ma.append(input())

t = []
for i in range(m):
    t.append(input())

ans = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        for k in range(m):
            ll = ma[i + k][j: j + m]
            if ll != t[k]:
                break
        else:
            ans = True

if ans:
    print("Yes")
else:
    print("No")
