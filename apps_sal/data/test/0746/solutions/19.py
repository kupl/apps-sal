import math

a, b = [int(x) for x in input().split()]
n = int(input())
d = [[0, 0, 0] for i in range(n)]
for i in range(n):
	d[i] = [int(x) for x in input().split()]
mini = 1e9
for i in range(n):
	rasst = (d[i][0] - a)*(d[i][0] - a) + (d[i][1] - b)*(d[i][1] - b)
	mini = min(mini, math.sqrt(rasst)/d[i][2])
print(mini)

