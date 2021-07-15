N = int(input())
nums = [int(s) for s in input().split()]
nums = sorted(nums, reverse=True)

Alice = 0
Bob = 0
i = 0
while nums:
    if i % 2 == 0:
        Alice += nums.pop(0)
    else:
        Bob += nums.pop(0)
    i += 1

print(Alice-Bob)
