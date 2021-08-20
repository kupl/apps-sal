n = int(input())
n_all = 10 ** n
n_e0 = 9 ** n
n_e9 = 9 ** n
n_e09 = 8 ** n
ans = (n_all - n_e0 - n_e9 + n_e09) % (10 ** 9 + 7)
print(ans)
