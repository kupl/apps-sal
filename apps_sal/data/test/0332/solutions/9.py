import sys
n, m = list(map(int, input().split()))
m1 = [list(map(int, input().split())) for i in range(n)]
m2 = [list(map(int, input().split())) for i in range(n)]
for j in range(m + n - 1):
    x1 = {}
    x2 = {}
    for i in range(j + 1):
        if j - i < n and i < m:
            x1[m1[j - i][i]] = 0
            x2[m2[j - i][i]] = 0
    for i in range(j + 1):
        if j - i < n and i < m:
            x1[m1[j - i][i]] += 1
            x2[m2[j - i][i]] += 1
    if x1 != x2:
        print("NO")
        return
print("YES")
