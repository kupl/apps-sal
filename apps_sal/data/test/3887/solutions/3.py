import sys

input = sys.stdin.readline()

possible = False
input = "+ " + input.strip()
inparse = input.split(' ')
n = int(inparse[-1])
items = inparse[0:-2]
nums = []
for i in range(0, int(len(items) / 2)):
    if (items[i * 2] == '+'):
        nums.append(1)
    else:
        nums.append(-1)
sumnum = sum(nums)

while (sumnum != n):
    found = False
    deficit = abs(sumnum - n)
    if (sumnum < n):
        for i in range(0, len(nums)):
            if nums[i] < n and nums[i] >= 1:
                nums[i] = min(nums[i] + deficit, n)
                found = True
                break
    elif (sumnum > n):
        for i in range(0, len(nums)):
            if nums[i] > -1 * n and nums[i] <= -1:
                nums[i] = max(nums[i] - deficit, -1 * n)
                found = True
                break
    sumnum = sum(nums)
    if not found:
        break

if sumnum == n:
    possible = True

if possible:
    print("Possible")
    outstr = ""
    for i in nums:
        if i > 0:
            outstr = outstr + ' + ' + str(abs(i))
        else:
            outstr = outstr + ' - ' + str(abs(i))
    outstr = outstr + " = " + str(n)
    print(outstr.strip()[2:])
else:
    print("Impossible")
