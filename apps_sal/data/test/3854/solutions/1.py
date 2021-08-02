n, k = list(map(int, input().split()))
cs = list(map(int, input().split()))

# table[c][s] has bit ss set if can make subset s and sub-subset ss
# using only the first c coins.
# We only ever need to know table[c-1] to compute table[c].
table = [[0 for _ in range(k + 1)] for _ in range(2)]

# Can always make subset 0 and sub-subset 0 using 0 coins.
table[0][0] = 1

for i, c in enumerate(cs, 1):
    for s in range(k + 1):
        # Include the coin in neither subset nor sub-subset.
        table[i % 2][s] |= table[(i - 1) % 2][s]
        if c <= s:
            # Include the coin in subset but not sub-subset.
            table[i % 2][s] |= table[(i - 1) % 2][s - c]
            # Include the coin in both the subset and sub-subset.
            table[i % 2][s] |= (table[(i - 1) % 2][s - c] << c)

possible = [str(i) for i in range(k + 1) if (table[n % 2][k] >> i) & 1]
print(len(possible))
print(*possible)
