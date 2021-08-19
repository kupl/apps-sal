num = int(input())
result = 2 * (10 ** num - 9 ** num) - (10 ** num - 8 ** num)
print(str(result % 1000000007))
