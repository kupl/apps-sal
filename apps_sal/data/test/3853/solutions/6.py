import math
t = int(input())
ans = -1
maxi = -1
for i in range(t):
    (k, a) = list(map(int, input().split()))
    h = k + math.ceil(math.log(a, 4))
    ans = max(ans, h)
    maxi = max(maxi, k)
print(max(ans, maxi + 1))
