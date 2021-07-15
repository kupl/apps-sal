n = int(input())
left = 1
right = n ** 2
for i in range(n):
    for j in range(n // 2):
        print(left, right, end=' ')
        left, right = left + 1, right - 1
    print()
