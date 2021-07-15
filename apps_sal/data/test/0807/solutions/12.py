#fn(pi) = pi-(pi+1)-c
#determine fn(pi) when it is max.

n,c = [v for v in map(int,input().split())]
p = [v for v in map(int,input().split())]
profit = lambda i: p[i] - (p[i+1]) - c
max_profit = 0
for i in range(n-1):
	pr = profit(i)
	if(pr > max_profit):
		max_profit = pr
print(max_profit)



