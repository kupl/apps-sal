def get_multypler(k, a, b):
    res = (10 ** k - 1) // a + 1
    bad_residue = (a - ((10 ** (k - 1)) * b) % a) % a
    suf = (10 ** (k - 1)) - 1
    minus = suf // a + (1 if (bad_residue <= suf % a) else 0)
    return res - minus


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 1
for i in range(n // k):
    ans *= get_multypler(k, a[i], b[i])
    ans %= 10 ** 9 + 7

print(ans)
