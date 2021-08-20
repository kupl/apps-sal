n = int(input())
a = sorted(list(map(int, input().split())))
if a[0] != a[1] and a[1] != a[2]:
    print(a.count(a[2]))
elif a[0] != a[1] and a[1] == a[2]:
    t = a.count(a[1])
    print(t * (t - 1) // 2)
elif a[0] == a[1] and a[1] != a[2]:
    print(a.count(a[2]))
else:
    t = a.count(a[0])
    print(t * (t - 1) * (t - 2) // 6)
