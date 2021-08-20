from collections import Counter
(n, a) = (int(input()), sorted(map(int, input().split())))
if n == 1:
    print(-1)
elif a[0] == a[-1]:
    print(1)
    print(a[0])
else:
    d = Counter((a[i + 1] - a[i] for i in range(n - 1)))
    if len(d) == 1:
        v = [2 * a[0] - a[1], 2 * a[-1] - a[-2]]
        if len(a) == 2 and sum(a) % 2 == 0:
            v.insert(1, (a[0] + a[1]) // 2)
        print(len(v))
        print(' '.join(map(str, v)))
    else:
        k = sorted(d.keys())
        if len(d) == 2 and d[k[1]] == 1 and (k[1] == 2 * k[0]):
            for i in range(n - 1):
                if a[i + 1] - a[i] == k[1]:
                    print(1)
                    print(a[i] + k[0])
        else:
            print(0)
