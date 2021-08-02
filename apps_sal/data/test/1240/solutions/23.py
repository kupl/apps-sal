n = int(input())
l, r = 0, 0
a = []
for i in range(n):
    l_i, r_i = map(int, input().split())
    l += l_i
    r += r_i
    a.append([l_i, r_i])
ans = abs(l - r)
ind = 0
for i in range(n):
    if (abs(l - a[i][0] + a[i][1] - (r - a[i][1] + a[i][0])) > ans):
        ans = abs(l - a[i][0] + a[i][1] - (r - a[i][1] + a[i][0]))
        ind = i + 1
print(ind)
