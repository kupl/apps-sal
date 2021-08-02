nums = [int(e) for e in input().split()]

Sheep = nums[0]
Wolves = nums[1]

if Sheep > Wolves:
    print("safe")
else:
    print("unsafe")
