import math
N = int(input())
List = list(map(int, input().split()))
mid = List[0]
for i in range(1, N):
    mid = mid * List[i] // math.gcd(mid, List[i])
res = 0
for i in range(N):
    res += (mid - 1) % List[i]
print(res)
