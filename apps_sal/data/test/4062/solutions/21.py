(a, b, c, d) = input().split()
x = [int(a), int(b)]
y = [int(c), int(d)]
nums = []
for i in range(len(x)):
    for j in range(len(y)):
        num = x[i] * y[j]
        nums.append(num)
max_num = max(nums)
print(max_num)
