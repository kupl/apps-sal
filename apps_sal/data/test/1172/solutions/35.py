S = input()
mod = 10 ** 9 + 7

a, ab, abc, n = 0, 0, 0, 1
for s in S:
    if s == "A":
        a += n
        a %= mod
    elif s == "B":
        ab += a
        ab %= mod
    elif s == "C":
        abc += ab
        abc %= mod
    else:
        a, ab, abc, n = 3 * a + n, 3 * ab + a, 3 * abc + ab, 3 * n
        a %= mod
        ab %= mod
        abc %= mod
        n %= mod

print(abc)
