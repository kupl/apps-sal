n = int(input())
res = 0
res += 8 * (3 * pow(4, n - 3))
res += (n - 3) * 4 * 9 * int(pow(4, n - 4))
print(res)
