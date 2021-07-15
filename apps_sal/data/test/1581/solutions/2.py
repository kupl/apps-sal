from itertools import accumulate

N,K = map(int, input().split())
mod = 10**9+7
sqt = int(N**0.5)
cnt = [N // i-N // (i+1) for i in range(1, N//sqt)] + [1]*sqt
x = cnt
for _ in range(K):
    x = [(i*j)%mod for i, j in zip(accumulate(reversed(x)), cnt)]
    

print(x[-1])
