N = int(input())
nums = [int(s) for s in input().split()]
i = 0
cnt = 0
while True:
    if i == N:
        i = 0
        cnt += 1
    if nums[i % N] % 2 == 1:
        break
    nums[i % N] //= 2
    i += 1
print(cnt)
