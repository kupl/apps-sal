N = int(input())
num = list(range(1, N + 1))
num1 = [i for i in num if (i % 3 != 0 and i % 5 != 0)]
print(sum(num1))
