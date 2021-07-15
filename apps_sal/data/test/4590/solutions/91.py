from itertools import accumulate
import bisect
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_c = [0] + list(accumulate(a))
b_c = [0] + list(accumulate(b))

result = []

for i in range(n+1):
    if k >= a_c[i]:
        k_temp = k - a_c[i]
        b_idx = bisect.bisect_left(b_c, k_temp+1)
        result.append(i + b_idx - 1)
    else:
        pass
result.append(0)
print(max(result))
