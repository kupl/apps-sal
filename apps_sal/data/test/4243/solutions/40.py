X = int(input())

res = X // 500 * 1000
X %= 500
res += X // 5 * 5

print(res)
