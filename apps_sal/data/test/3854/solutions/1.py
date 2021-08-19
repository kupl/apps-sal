(n, k) = list(map(int, input().split()))
cs = list(map(int, input().split()))
table = [[0 for _ in range(k + 1)] for _ in range(2)]
table[0][0] = 1
for (i, c) in enumerate(cs, 1):
    for s in range(k + 1):
        table[i % 2][s] |= table[(i - 1) % 2][s]
        if c <= s:
            table[i % 2][s] |= table[(i - 1) % 2][s - c]
            table[i % 2][s] |= table[(i - 1) % 2][s - c] << c
possible = [str(i) for i in range(k + 1) if table[n % 2][k] >> i & 1]
print(len(possible))
print(*possible)
