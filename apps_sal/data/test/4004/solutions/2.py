n = int(input())
a = list(map(int, input().split()))
s = set(a)
if len(s) > 3:
    print(-1)
elif len(s) == 1:
    print(0)
elif len(s) == 2:
    a = list(s)
    d = abs(a[0] - a[1])
    if d % 2 == 0:
        d //= 2
    print(d)
else:
    a = sorted(list(s))
    if a[1] - a[0] == a[2] - a[1]:
        print(a[1] - a[0])
    else:
        print(-1)
