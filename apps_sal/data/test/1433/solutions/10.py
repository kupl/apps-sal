n, m = map(int, input().split())
a = []
t_a = []
ans = 0

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

t_a = list(map(list, zip(*a)))
# print(a)
# print(t_a)
for i in range(n):
    c = a[i].count(1)
    if (c > 1):
        l = a[i].index(1)
        r = m - a[i][::-1].index(1) - 1
        #print(l, r, ((m - c - (l + (m - r - 1)))))
        ans += l + (m - r - 1) + ((m - c - (l + (m - r - 1))) * 2)
    elif (c == 1):
        ans += m - 1
    # print(ans)

for i in range(m):
    c = t_a[i].count(1)
    if (c > 1):
        l = t_a[i].index(1)
        r = n - t_a[i][::-1].index(1) - 1
        ans += l + (n - r - 1) + ((n - c - (l + (n - r - 1))) * 2)
    elif (c == 1):
        ans += n - 1
    # print(ans)
print(ans)
