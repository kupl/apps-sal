n, m = list(map(int, input().split()))
n_one = len(input().strip()) - (2 * n - 1)
less = min(n_one, n - n_one) * 2
res = [None] * m

for i in range(0, m):
    l, r = list(map(int, input().split()))
    q = r - l + 1
    res[i] = '1' if q % 2 == 0 and q <= less else '0'

print('\n'.join(res))

