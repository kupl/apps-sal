n, m = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))
money = list(map(int, input().split(' ')))

res = 0
cur = 0
for price in prices:
	if money[cur] >= price:
		res += 1
		cur += 1
	if cur >= len(money):
		break
print(res)

