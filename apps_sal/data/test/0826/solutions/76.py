n = int(input())
ans = 0
target = int((2 * (n + 1)) ** 0.5)
for num in range(max(target - 1000, 1), target + 1000):
    if num * (num + 1) > 2 * (n + 1):
        break
    else:
        ans = num
print(n - ans + 1)
