import math
import itertools

n = int(input())
a = list(map(int, input().split()))
pf = [0] + list(itertools.accumulate(a, math.gcd))
pb = [0] + list(itertools.accumulate(reversed(a), math.gcd))
pb.reverse()
ans = [0] * n
for i in range(n):
    ans[i] = math.gcd(pf[i], pb[i + 1])
print(max(ans))
