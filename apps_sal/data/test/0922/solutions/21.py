n,A = map(int,input().split())
d =  [int(x) for x in input().split()]
s = sum(d)
ans = []
for i in d:
	ss = A - n + 1 #require when another 1
	sd = s - i - (n - 1) #another +-
	if(ss <= 0 or A > s):
		ans.append(i)
	else:
		l = max(A - s + i,1)
		r = min(ss,i)
		ans.append(i-r+l-1)
print(''.join([str(ans[i])+' 'for i in range(n)]))
