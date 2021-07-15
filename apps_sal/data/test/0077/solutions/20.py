n = int(input())
nums = [int(i) for i in input().split()]
result = 0
min_positive = 10001
max_negative = -10001
for i in nums:
    if i > 0:
        result += i
    if i % 2 == 1:
        if 0 < i < min_positive:
            min_positive = i
        elif max_negative < i < 0:
            max_negative = i
if result % 2 == 0:
    if abs(max_negative) > min_positive:
        result -= min_positive
    else:
        result += max_negative
print(result)

