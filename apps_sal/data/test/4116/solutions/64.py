# 因数分解して、入れ子で掛け算して、inで入ってるか見る

N = int(input())

nums = []
mul = []

for i in range(1, 9 + 1):
    if N % i == 0:
        nums.append(i)
    else:
        pass

# print(nums)


for i in nums:
    for j in nums:
        mul.append(i * j)

# print(mul)


if N in mul:
    print('Yes')
else:
    print('No')
