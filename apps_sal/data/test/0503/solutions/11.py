from sys import stdin, stdout
from collections import defaultdict

n,k = [int(x) for x in stdin.readline().rstrip().split()]
nums = [int(x) for x in stdin.readline().rstrip().split()]

a=defaultdict(lambda: 0)
b=defaultdict(lambda: 0)

ans = 0

for i in range(n):
    num = nums[i]
    if num % k == 0:
        ans += b[int(num/k)]
        b[num] += a[int(num/k)]
    a[num]+=1
print(ans)
