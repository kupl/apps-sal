def canBuy(k):
	fullCost = [(i + 1) * k + cost[i] for i in range(0, n)]
	fullCost = sorted(fullCost)
	fullSum = sum(fullCost[:k])
	return fullSum <= money

def canBuyCost(k):
	fullCost = [(i + 1) * k + cost[i] for i in range(0, n)]
	fullCost = sorted(fullCost)
	fullSum = sum(fullCost[:k])
	return fullSum if fullSum <= money else -1

n, money = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]

left = 0
right = n
while left < right - 1:
	mid = (left + right) // 2
	if canBuy(mid):
		left = mid
	else:
		right = mid

rightRes = canBuyCost(right)
if rightRes == -1:
	print(left, canBuyCost(left))
else:
	print(right, rightRes)
