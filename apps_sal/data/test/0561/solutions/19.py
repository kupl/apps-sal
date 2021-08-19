n = int(input())
a = sorted(map(int, input().split()))
if n < 2:
    print(-1)
else:
    count = {}
    I = range(n - 1)
    for i in I:
        d = a[i + 1] - a[i]
        count[d] = count.get(d, 0) + 1
    d = min(count)
    if count[d] < n - 2:
        print(0)
    else:
        b = set()
        if count[d] + 1 == n:
            b.add(int(a[0] * 2 - a[1]))
            b.add(int(a[-1] * 2 - a[-2]))
        for i in I:
            e = a[i + 1] - a[i]
            if not e % 2:
                f = e / 2
                count[f] = count.get(f, 0) + 2
                count[e] -= 1
                if count[min(d, f)] == n:
                    b.add(int(a[i] + f))
                count[e] += 1
                count[f] -= 2
        print(len(b))
        print(' '.join(map(str, sorted(b))))
