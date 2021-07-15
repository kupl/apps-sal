a, b = map(int, input().split())
if b - a > 10:
    print(0)
else:
    mul = 1
    for i in range(a + 1, b + 1):
        mul *= i
    print(mul % 10)
