A, B = list(map(int, input().split()))
ans = 0

for nums in range(A, B + 1):
    nums = str(nums)
    if nums == nums[::-1]:
        ans += 1

print(ans)
