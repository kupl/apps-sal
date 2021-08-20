N = int(input())
nums = []
mul = []
for i in range(1, 9 + 1):
    if N % i == 0:
        nums.append(i)
    else:
        pass
for i in nums:
    for j in nums:
        mul.append(i * j)
if N in mul:
    print('Yes')
else:
    print('No')
