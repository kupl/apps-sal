import re
import copy


def accept_input():
    (N, K) = list(map(int, input().split()))
    return (N, K)


(N, K) = accept_input()
if K == 1:
    print(N)
else:
    print(K * (K - 1) ** (N - 1))
