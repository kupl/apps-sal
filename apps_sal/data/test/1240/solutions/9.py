n = int(input())
a = []
sl = 0
sr = 0
for i in range(n):
    q, w = list(map(int, input().split()))
    a += [(q, w)]
    sl += q
    sr += w
cur = abs(sr - sl)
m = 0
for i in range(n):
    if abs((sl - a[i][0] + a[i][1]) - (sr - a[i][1] + a[i][0])) > cur:
        cur = abs((sl - a[i][0] + a[i][1]) - (sr - a[i][1] + a[i][0]))
        m = i + 1
print(m)
