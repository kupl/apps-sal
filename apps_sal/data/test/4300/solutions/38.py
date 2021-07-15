N = int(input())
D = list(map(int, input().split()))
from itertools import accumulate
print((sum(list(d*c for d, c in zip(D[1:], accumulate(D))))))

