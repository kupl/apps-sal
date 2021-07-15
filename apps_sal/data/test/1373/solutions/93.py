from itertools import accumulate

# k個選んだ時の最小値と最大値が分かれば、個数が分かる？？
n,k = list(map(int, input().split()))
cumsum   = list(accumulate(range(n+1)))
cumsum_r = list(accumulate(range(n+1)[::-1]))

MOD = 10**9 + 7
ans = 0
for i in range(k, n+2):
    _min, _max = cumsum[i-1], cumsum_r[i-1]
    ans = (ans + _max - _min + 1) % MOD

print(ans)
