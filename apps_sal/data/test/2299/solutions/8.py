def ri():
    return list(map(int, input().split()))


n, m = ri()
a = []
for i in range(n):
    a.append(list(ri()))

t = [[0 for i in range(m)] for j in range(n)]
T = [0 for i in range(n)]

for i in range(m):
    for j in range(n - 1):
        if a[j][i] > a[j + 1][i]:
            t[j + 1][i] = 0
        else:
            t[j + 1][i] = t[j][i] + 1
for i in range(n):
    T[i] = max(t[i])

k = int(input())
ans = []
for i in range(k):
    l, r = ri()
    l = l - 1
    r = r - 1
    if T[r] >= r - l:
        ans.append("Yes")
    else:
        ans.append("No")

print('\n'.join(ans))
