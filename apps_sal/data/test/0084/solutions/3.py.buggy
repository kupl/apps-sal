n = int(input())
if n < 5:
    print(n * (n - 1) // 2)
    return
s0 = str(n + n - 1)
k = len(s0)
if s0 != k * '9':
    k -= 1
s = k * '9'


def cnt(s):
    v = int(s)
    # print(v)
    if v > n * 2 - 1:
        return 0
    if v == 2 * n - 1:
        return 1
    if v > n:
        return n - v // 2
    if v <= n:
        return v // 2


ans = cnt(s)
for i in range(1, 9):
    ans += cnt(str(i) + s)
print(ans)
