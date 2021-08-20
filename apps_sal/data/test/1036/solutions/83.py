from typing import List


def winner(a: str, b: str) -> str:
    return b if (a, b) in [('R', 'P'), ('P', 'S'), ('S', 'R')] else a


def rec(k, offset):
    if k == 0:
        return S[offset]
    elif memo[k][offset] != '?':
        return memo[k][offset]
    former = rec(k - 1, offset)
    latter = rec(k - 1, (offset + p2[k - 1]) % N)
    memo[k][offset] = winner(former, latter)
    return memo[k][offset]


(N, K) = list(map(int, input().split()))
S: List[str] = list(input())
p2 = [1]
for k in range(K):
    p2.append(p2[-1] * 2 % N)
memo = [['?'] * (N + 1) for _ in range(K + 1)]
rec(K, 0)
print(memo[K][0])
