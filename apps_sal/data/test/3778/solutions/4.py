n = int(input())
a = list(map(int, input().split()))
right_free = [] # dlya 2
right_busy = [] # dlya 3
ans = []
for i in range(n-1, -1, -1):
	if a[i] == 1:
		right_free.append(i)
	elif a[i] == 2:
		right_busy.append(i)
		if not right_free:
			print(-1)
			return
		x = right_free.pop()
		ans.append([i, i])
		ans.append([i, x])
	elif a[i] == 3:
		if not right_busy and not right_free:
			print(-1)
			return
		if right_busy:
			x = right_busy.pop()
			ans.append([i, i])
			ans.append([i, x])
		else:
			x = right_free.pop()
			ans.append([i, i])
			ans.append([x, x])
			ans.append([i, x])
		right_busy.append(i)
while right_free:
	x = right_free.pop()
	ans.append([x, x])
print(len(ans))
for x,y in ans:
	print(x+1, y+1)


