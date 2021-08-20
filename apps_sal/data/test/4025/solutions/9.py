(a, b, c) = list(map(int, input().split()))
week = [0, 1, 2, 0, 2, 1, 0]
nums = [3, 2, 2]
num = min(min(a // nums[0], b // nums[1]), c // nums[2])
num2 = [a - nums[0] * num, b - nums[1] * num, c - nums[2] * num]
ans = 0
for j in range(7):
    num3 = [num2[0], num2[1], num2[2]]
    i = j
    temp = num * 7
    while True:
        if num3[week[i]] == 0:
            break
        num3[week[i]] -= 1
        temp += 1
        i += 1
        i %= 7
    ans = max(temp, ans)
print(ans)
