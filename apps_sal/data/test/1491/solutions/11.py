n = int(input())
li = input().strip().split(' ')
nums = []
ct = 0
zeros = 0
for i in li:
    i = int(i)
    if i == 0: zeros += 1
    if round(i**0.5)**2 == i: ct += 1
    tmp = int(i**0.5)
    nums.append(min(i - tmp * tmp, (tmp + 1)**2 - i))
nums.sort()
half = int(n / 2)
if ct <= half: print(sum(nums[:half]))
else:
    rst = ct - half
    if zeros > half:
        rst += zeros - half
    print(rst)
