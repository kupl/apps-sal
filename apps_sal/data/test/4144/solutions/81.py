n = int(input())
ans = 10 ** n - 2 * pow(9, n) + 8 ** n
k = pow(10, 9) + 7
print(ans % k)
