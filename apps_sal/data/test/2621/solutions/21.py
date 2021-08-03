def func(m, k, a):
    for i in range(len(a) - 1):
        if a[i] + k >= a[i + 1]:
            m += a[i] - max(0, a[i + 1] - k)
        else:
            m = m - max(a[i + 1] - k - a[i], 0)
            if m < 0:
                return 0
    return 1


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = func(m, k, a)
    if res:
        print("YES")
    else:
        print("NO")
