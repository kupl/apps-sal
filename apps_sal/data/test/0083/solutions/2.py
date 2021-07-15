n = int(input())
a = [int(i) for i in input().split()]
minus = 0
plus = 0
for el in a:
    if el > 0:
        minus += 1
    elif el < 0:
        plus += 1
if minus >= n // 2 + n % 2:
    print(1)
elif plus >= n // 2 + n % 2:
    print(-1)
else:
    print(0)

