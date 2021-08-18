from collections import Counter
import math
import statistics
import itertools
H, W, K = list(map(int, input().split()))
two = [list(input()) for _ in range(H)]

ans = 0
for i in range(2**H):
    for j in range(2**W):
        count = 0
        for h in range(H):
            for w in range(W):
                if (i >> h) & 1 == 1 and (j >> w) & 1 == 1:
                    if two[h][w] == "
                    count += 1

        if count == K:
            ans += 1

print(ans)
