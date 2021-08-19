(n, k) = map(int, input().split())
nums = list(map(int, input().split()))
now = 0
i = 0
while 1 == 1:
    i += 1
    now += i
    if now >= k:
        now -= i
        k -= now
        break
print(nums[k - 1])
