from collections import defaultdict
import numpy as np
import collections

N = int(input())
As = list(map(int, input().split()))

B = defaultdict(int)

ans = 0

for index, A in enumerate(As):
    ans += B[index - A]

    B[index + A] += 1

print(ans)
