(n, number) = map(int, input().split())
if number % 2:
    print(number // 2 + 1)
else:
    print((n - number) // 2 + 1)
