n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
s1 = sum([x[0] for x in a])
a.sort(key=lambda x: x[1] / x[0])

ans = 10**9
s2 = 0
l = -1
for i in range(n):
    if s2 + a[i][1] <= s1 - a[i][0]:
        s2 += a[i][1]
        s1 -= a[i][0]
        l = i
if l != -1 and a[l][0] == 1:
    for i in range(l + 1, n):
        if a[i][0] == 2 and s2 - a[l][1] + a[i][1] <= s1 - 1:
            print(s1 - 1)
            return
print(s1)

