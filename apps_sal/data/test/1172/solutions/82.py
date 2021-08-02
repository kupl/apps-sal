S = input(); N = len(S)
a, b, c, d = 0, 0, 0, 1
mod = 10**9 + 7
for x in reversed(S):
    if x == "?":
        a, b, c, d = (3 * a + b) % mod, (3 * b + c) % mod, (3 * c + d) % mod, 3 * d % mod
    elif x == "A": a = (a + b) % mod
    elif x == "B": b = (b + c) % mod
    elif x == "C": c = (c + d) % mod
print(a)
