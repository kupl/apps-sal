(n, k) = [int(x) for x in input().split()]
nums = sorted([int(x) for x in input().split()])
count = [0 for _ in range(2 * 100000 + 10)]
ops = [0 for _ in range(2 * 100000 + 10)]
for num in nums:
    op = 0
    while num > 0:
        ops[num] += op if count[num] < k else 0
        count[num] += 1
        num = num // 2
        op += 1
    ops[num] += op if count[num] < k else 0
    count[num] += 1
minn = 0
minop = ops[0]
for i in range(2 * 100000 + 1):
    if count[i] >= k and ops[i] < minop:
        minn = i
        minop = ops[i]
print(minop)
