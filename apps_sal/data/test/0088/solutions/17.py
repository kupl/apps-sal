a, b = list(map(int, input().split()))
print(sum((2 ** i - 1) ^ 2 ** j in range(a, b + 1) for i in range(2, 65) for j in range(i - 1)))

