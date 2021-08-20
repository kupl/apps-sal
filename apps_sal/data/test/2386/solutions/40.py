n = int(input())
a = [ai - i for (ai, i) in zip(map(int, input().split()), [j for j in range(1, n + 1)])]
a.sort()
if n % 2:
    b = a[n // 2]
    print(sum([abs(ai - b) for ai in a]))
else:
    (b1, b2) = (a[n // 2 - 1], a[n // 2])
    print(min(sum([abs(ai - b1) for ai in a]), sum([abs(ai - b2) for ai in a])))
