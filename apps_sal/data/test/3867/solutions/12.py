n = int(input())
fst, nxt, lst, des = [0 for i in range(2 * n + 1)], [0 for i in range(2 * n + 1)], [0 for i in range(2 * n + 1)], [0 for i in range(2 * n + 1)]
cnt = 0

def add(u, v) :
	nonlocal cnt
	cnt += 1
	if fst[u] == 0 :
		fst[u] = cnt
	else :
		nxt[lst[u]] = cnt
	lst[u], des[cnt] = cnt, v

for i in range(1, n) : 
	u, v = list(map(int, input().split()))
#	print(u, v)
	add(u, v)
	add(v, u)

a = list(map(int, input().split()))
deep = [0 for i in range(n + 1)]
deep[1] = 1
now, res = 1, 1
Ans = 0

for i in range(0, n) :
	if deep[a[i]] == 0 : 
		Ans = 1
		break
	elif deep[a[i]] < now :
		Ans = 1
		break
	else : 
		b = fst[a[i]]
		res += 1
		while b > 0 :
			if deep[des[b]] == 0 : 
				deep[des[b]] = res
			b = nxt[b]
		now = deep[a[i]]

if Ans == 0 :
	print("Yes")
else :
	print("No")

