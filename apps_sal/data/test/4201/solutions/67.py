from collections import Counter
import math
import statistics
import itertools
H, W, K = list(map(int, input().split()))
# b=int(input())
# c=[]
# for i in a:
#     c.append(int(i))
# A,B,C= map(int,input().split())
# f = list(map(int,input().split()))
#g = [list(map(lambda x: '{}'.format(x), list(input()))) for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
two = [list(input()) for _ in range(H)]  # nizigen

ans = 0
for i in range(2**H):
    for j in range(2**W):
        count = 0
        for h in range(H):
            for w in range(W):
                if (i >> h) & 1 == 1 and (j >> w) & 1 == 1:
                    if two[h][w] == "#":
                        count += 1

        if count == K:
            ans += 1

print(ans)
