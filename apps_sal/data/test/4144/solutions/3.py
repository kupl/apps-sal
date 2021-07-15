N = int(input())
val = 7 + 10 ** 9

print(((pow(10, N, val) - pow(9, N, val) * 2 + pow(8, N, val)) %val ))

