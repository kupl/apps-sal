import sys
import math
n = int(input())
z = list(map(int, input().split()))
a = z[0]
ans = [1]
sum_ = a
sum_s = a
for i in range(1, n):
    sum_s += z[i]
    if z[i] * 2 <= a:
        ans.append(i + 1)
        sum_ += z[i]
if sum_ * 2 > sum_s:
    print(len(ans))
    print(*ans)
else:
    print(0)
