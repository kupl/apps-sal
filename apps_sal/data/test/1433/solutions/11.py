def count_place(a, n, m):
    place = 0
    for i in range(n):
        c = a[i].count(1)
        if c > 1:
            l = a[i].index(1)
            r = m - a[i][::-1].index(1) - 1
            place += l + (m - r - 1) + (m - c - (l + (m - r - 1))) * 2
        elif c == 1:
            place += m - 1
    return place


(n, m) = map(int, input().split())
a = []
t_a = []
ans = 0
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
t_a = list(map(list, zip(*a)))
ans = count_place(a, n, m) + count_place(t_a, m, n)
print(ans)
