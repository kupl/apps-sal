#import math
X, Y = map(int, input().split())
cnt = 0

#ans = int(math.log2(Y) - math.log2(X))
# print(ans+1)
while X <= Y:
    X *= 2
    cnt += 1
print(cnt)
