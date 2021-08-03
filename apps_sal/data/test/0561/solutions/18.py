n = int(input())
a = sorted((list(map(int, input().split()))))
if n == 1:
    print(-1)
else:
    if a[0] == a[-1]:
        p = [a[0]]
    else:
        p = []
        d = list(set(a[i + 1] - a[i] for i in range(n - 1)))
        if len(d) == 1:
            p = [a[0] - d[0], a[-1] + d[0]]
            if n == 2 and (a[1] - a[0]) % 2 == 0:
                p += [(a[1] + a[0]) // 2]
            # print(p)
        elif len(d) == 2:
            if max(d) == 2 * min(d):
                for i in range(n - 1):
                    if a[i + 1] - a[i] == max(d):
                        if len(p) == 0:
                            p = [(a[i + 1] + a[i]) // 2]
                        else:
                            p = []
                            break
    print(len(p))
    print(' '.join(map(str, sorted(p))))
