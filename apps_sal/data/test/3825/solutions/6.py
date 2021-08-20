n = int(input())
if n > 20:
    print(733 + (n - 20) * 49)
else:
    s = set()
    for i in range(n + 1):
        for v in range(n - i + 1):
            for x in range(n - i - v + 1):
                l = n - i - v - x
                s.add(i + 5 * v + 10 * x + 50 * l)
    print(len(s))
