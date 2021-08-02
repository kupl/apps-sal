n = int(input())
a = sorted(set(map(int, input().split())))
if len(a) > 3:
    print(-1)
elif len(a) == 3:
    print(-1 if 3 * a[1] != sum(a) else a[2] - a[1])
elif len(a) == 2:
    print(a[1] - a[0] if (a[1] - a[0]) % 2 else (a[1] - a[0]) // 2)
else:
    print(0)
