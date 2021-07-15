def __starting_point():
	n = int(input())
	v = list(map(int, input().split()))
	t = list(map(int, input().split()))
	l = []
	ans = []
	for i in range (n):
		cancel = 0
		if i == 0:
			if v[i] <= t[i]:
				cancel+=v[i]
				v[i]-=v[i]
			else:
				cancel +=t[i]
				v[i]-=t[i]
			l.append(v[i])
			ans.append(cancel)
		else:
			l.append(v[i])
			j = 0
			while j < len(l):
				if l[j] == 0:
					l.pop(j)
					j-=1
				elif l[j] <= t[i]:
					cancel += l[j]
					l[j]-=l[j]
				else:
					cancel+=t[i]
					l[j]-=t[i]
				j+=1
			ans.append(cancel)
	print(*ans)
__starting_point()
