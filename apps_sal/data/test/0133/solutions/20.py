mod = 10 ** 9 + 7
n, m = list(map(int, input().split()))
print(pow((pow(2, m, mod) - 1), n, mod))

