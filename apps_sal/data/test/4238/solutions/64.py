N = input()
nums = []
length = len(N)
for i in range(1, length + 1):
    value = int(N[-i])
    nums.append(value)
sumOfNums = sum(nums)
if sumOfNums % 9 == 0:
    print('Yes')
else:
    print('No')
