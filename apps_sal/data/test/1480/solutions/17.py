n,k = list(map(int,input().split()))
a = [int(x) for x in input().split()]
v = [i for i in range(1,n+1)]
val = 0
ans = ""
for i in a:
	i %= len(v)
	val += i
	if val>=len(v): val -= len(v)
	ans += str(v[val]) + ' '
	del v[val]
	
print(ans)

