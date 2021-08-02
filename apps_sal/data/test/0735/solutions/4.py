sa = int(input())
sa2 = input().split(' ')
nums = [int(x) for x in sa2]
diffs = [nums[x + 1] - nums[x] for x in range(sa - 1)]

listx = [x for x in range(sa - 1) if diffs[x] < 0]

if listx == []:
    print("yes")
    print("1 1")
else:
    magic = nums[listx[0]:listx[-1] + 2]
    magic.reverse()
    nums[listx[0]:listx[-1] + 2] = magic

    mark = 0
    for t in range(sa - 1):
        if nums[t] - nums[t + 1] > 0:
            mark = 1
    if mark == 1:
        print("no")
    else:
        print("yes")
        print(listx[0] + 1, listx[-1] + 2)
