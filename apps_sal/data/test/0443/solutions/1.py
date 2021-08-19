n = int(input())
a = [int(v) for v in input().split()]
if n == 1:
    print(-1)
elif n == 2:
    if a[0] == a[1]:
        print(-1)
    else:
        print(1)
        print(1)
else:
    print(1)
    mini = None
    minv = 10000000
    for (i, v) in enumerate(a):
        if v < minv:
            minv = v
            mini = i
    print(mini + 1)
