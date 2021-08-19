# import
#import math
#import numpy as np
# = int(input())
S = input()
# = map(int, input().split())
# = list(map(int, input().split()))
# = [input(), input()]
# = [list(map(int, input().split())) for _ in range(N)]
# = [int(input()) for _ in range(N)]
# = {i:[] for i in range(N)}
ans = 0
for s in S:
    if s == "+":
        ans += 1
    else:
        ans -= 1

print(ans)
