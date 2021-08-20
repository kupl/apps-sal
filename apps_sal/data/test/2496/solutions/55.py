import numpy as np
N = int(input())
A = list(map(int, input().split()))
cnt = [0] * (10 ** 6 + 1)
for a in A:
    cnt[a] += 1
if np.gcd.reduce(A) != 1:
    print('not coprime')
elif np.all([sum(cnt[i::i]) <= 1 for i in range(2, 10 ** 6 + 1)]):
    print('pairwise coprime')
else:
    print('setwise coprime')
