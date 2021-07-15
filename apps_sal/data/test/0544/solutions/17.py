t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ok = True

    for i in range(n // 2):
        c1, c2 = s[i], s[n - i - 1]
        if abs(ord(c2) - ord(c1)) not in {0, 2}:
            ok = False
            break

    print(['NO', 'YES'][ok])

