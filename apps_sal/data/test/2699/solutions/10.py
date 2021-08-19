t = int(input())
nums = list(map(int, input().split()))
for i in nums:
    for row in range(1, 5):
        if row == 3:
            y = row + 1
            x = 3 * 2
        elif row == 4:
            y = row - 1
            x = 3
        else:
            y = row
            x = 3
        for col in range(1, i + 1):
            print(y, end=' ')
            y += x
            x *= 2
        print()
