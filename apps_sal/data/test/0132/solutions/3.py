n = int(input())

nums = list(map(int, input().split()))

answer = float('inf')

for l in range(n):
    for s in range(n):
        if(s + l - 1 >= n):continue
        current = sum(nums[s:s + l])
        answer = min(answer, abs(360 - 2 * current))


print(answer)

