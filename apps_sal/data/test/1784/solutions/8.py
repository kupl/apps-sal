(n, k) = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
pebbles = [[] for i in range(len(nums))]
smallest = min(nums)
prefix = smallest * [1]
nums = list([x - smallest for x in nums])
for c in range(1, k + 1):
    for (i, e) in enumerate(nums):
        if e != 0:
            pebbles[i].append(c)
            nums[i] -= 1
if any([x > 0 for x in nums]):
    print('NO')
else:
    print('YES')
    prefix = ' '.join(map(str, prefix))
    for p in pebbles:
        print(prefix + ' ' + ' '.join(map(str, p)))
