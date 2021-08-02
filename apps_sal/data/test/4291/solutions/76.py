n, q = map(int, input().split())
s = input()

nums = [0] * n
for i in range(1, n):
    if s[i] == "C":
        if s[i - 1] == "A":
            nums[i] += 1
    nums[i] += nums[i - 1]

for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(nums[r] - nums[l])
