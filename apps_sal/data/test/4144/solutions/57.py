N = int(input())
wari = 7 + 10 ** 9
print((pow(10, N, wari) - pow(9, N, wari) * 2 + pow(8, N, wari)) % wari)
