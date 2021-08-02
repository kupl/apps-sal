n, p = map(int, input().split())
t = [ord(c) - 97 for c in input()] + [27, 27]
for k in range(n - 1, -1, -1):
    for i in range(t[k] + 1, p):
        if i - t[k - 1] and i - t[k - 2]:
            a, b = min(t[k - 1], 2), min(i, 2)
            if a == b:
                a = 1
            t = t[: k] + [i] + [3 - a - b, a, b] * (n // 3 + 1)
            print(''.join(chr(i + 97) for i in t)[: n])
            return
print('NO')
