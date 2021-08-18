from collections import defaultdict

n = int(input())
nums = []
digits = defaultdict(int)
heads = set()
for i in range(n):
    nums.append(input())
    w = 1
    heads.add(nums[-1][0])
    for c in range(len(nums[-1]), 0, -1):
        digits[nums[-1][c - 1]] += w
        w *= 10

matching_digits = {}
result = sorted(list(digits.items()), key=lambda i: i[1])

matching_digits[result[-1][0]] = 1

for i in range(len(result) - 1, 0, -1):
    if result[i - 1][0] not in heads:
        matching_digits[result[i - 1][0]] = 0
        break

v = 2
for i in range(len(result) - 1, 0, -1):
    if not result[i - 1][0] in matching_digits:
        matching_digits[result[i - 1][0]] = v
        v += 1

sum = 0
for num in nums:
    sum += int(''.join(str(matching_digits[c]) for c in num))

print(sum)
