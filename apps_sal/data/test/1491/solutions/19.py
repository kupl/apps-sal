import math
n = int(input())
nums = [int(i) for i in input().split()]
a = [1000000000] * n
zero = 0
s = 0
for i in range(n):
    num = nums[i]
    k = int(math.sqrt(num))
    if k * k == num:
        if num == 0:
            zero += 1
        s += 1
    else:
        a[i] = min(num - k * k, (k + 1) * (k + 1) - num)
ans = 0
if s > n - s:
    delta = (s - (n - s)) // 2
    if delta <= s - zero:
        ans += delta
    else:
        ans += 2 * (delta - (s - zero)) + (s - zero)
else:
    delta = ((n - s) - s) // 2
    a.sort()
    ans = sum(a[:delta])
print(ans)
