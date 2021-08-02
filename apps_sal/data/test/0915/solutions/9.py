k = int(input())


def product(s):
    res = 1
    for e in s:
        res *= e
    return res


string = "codeforces"
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
index = 0
while True:
    p = product(nums)
    if p < k:
        nums[index] += 1
        index = (index + 1) % len(nums)
    else:
        break

result = ""
for i, e in enumerate(nums):
    result += e * string[i]

print(result)
