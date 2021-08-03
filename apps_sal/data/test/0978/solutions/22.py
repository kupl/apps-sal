nums = [0 for i in range(10)]
k = int(input())

for i in range(4):
    s = input()
    for c in s:
        if c != '.':
            nums[int(c)] += 1

if all(nums[i] <= 2 * k for i in range(10)):
    print('YES')
else:
    print('NO')
