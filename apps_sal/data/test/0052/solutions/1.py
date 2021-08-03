def calc(n):
    res = 0
    while n % 2 == 0:
        n //= 2
        res += n
    return res + n * (n - 1) // 2


def check(n, q):
    if 2 ** q - 1 > n:
        return None
    left = 0
    right = 10 ** 10
    def f(k): return k * (k - 1) // 2 + k * (2 ** q - 1)
    while left + 1 < right:
        mid = (left + right) // 2
        if f(mid) <= n:
            left = mid
        else:
            right = mid
    count = left * 2**q
    if calc(count) == n:
        return count
    else:
        return None


n = int(input())

ans = set()

# We want n=k*(k-1)/2 + k*(2^q-1)
for q in range(0, 64):
    k = check(n, q)
    if k:
        ans.add(k)

if ans:
    for i in sorted(ans):
        assert calc(i) == n, "n=%d, i=%d" % (n, i)
        print(i)
else:
    print(-1)
