from itertools import accumulate
N = int(input())
D = list(map(int, input().split()))
print((sum(list(d * c for d, c in zip(D[1:], accumulate(D))))))
