t = int(input())
for _ in range(t):
    x = input()
    a = int(x[0])
    b = len(x)
    print(10 * (a - 1) + b * (b + 1) // 2)
