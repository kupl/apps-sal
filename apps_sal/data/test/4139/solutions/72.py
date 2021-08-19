def generator(x, y):
    if 10 * x + 3 <= y:
        nums.append(10 * x + 3)
        nums.append(10 * x + 5)
        nums.append(10 * x + 7)


n = int(input())
nums = [3, 5, 7]
ans = 0
for num in nums:
    if num <= n and len(set(str(num))) == 3:
        ans += 1
    generator(num, n)
print(ans)
