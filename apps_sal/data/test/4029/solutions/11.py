n = input()
#if int(n) % 25 == 0:
#	print(0)
#	quit()

n = list(n)
if (not("5" in n)) and (not("0" in n)) and (not("7" in n)) and (not("2" in n)):
	print(-1)
	quit()
	
wkn = []
wkn[:] = n
ans = -1
for i in reversed(list(range(len(n)))):
	if (n[i] == "0"):
		wk1 = n[:i] + n[i + 1:] + [n[i]]
		ans = len(n) - i - 1
		if wk1[0] != "0":
			n[:] = wk1
			break
		else:
			count = 0
			f1 = True
			for j in wk1:
				count += 1
				if j != "0":
					f1 = False
					break
			if f1:
				ans = -1
				break
			ans += count - 1
			wk1 = [wk1[count - 1]] + wk1[:count - 1] + wk1[count:]
			n[:] = wk1
			break

if ans != -1:
	f = True
	for i in reversed(list(range(len(n) - 1))):
		if (n[i] == "0") or (n[i] == "5"):
			wk1 = n[:i] + n[i + 1:-1] + [n[i]]
			ans += len(n) - i - 2
			if wk1[0] != "0":
				f = False
				break
			else:
				count = 0
				f1 = True
				for j in wk1:
					count += 1
					if j != "0":
						f1 = False
						break
				if f1:
					ans = -1
					break
				ans += count - 1
				f = False
				break
	if f:
		ans = -1
			
wkans = ans

ans = -1
n = wkn
for i in reversed(list(range(len(n)))):
	if (n[i] == "5"):
		wk1 = n[:i] + n[i + 1:] + [n[i]]
		ans = len(n) - i - 1
		if wk1[0] != "0":
			n[:] = wk1
			break
		else:
			count = 0
			f1 = True
			for j in wk1:
				count += 1
				if j != "0":
					f1 = False
					break
			if f1:
				ans = -1
				break
			ans += count - 1
			wk1 = [wk1[count - 1]] + wk1[:count - 1] + wk1[count:]
			n[:] = wk1
			break
			
if ans != -1:
	f = True
	for i in reversed(list(range(len(n) - 1))):
		if (n[i] == "7") or (n[i] == "2"):
			wk1 = n[:i] + n[i + 1: -1] + [n[i]]
			ans += len(n) - i - 2
			if wk1[0] != "0":
				f = False
				break
			else:
				count = 0
				f1 = True
				for j in wk1:
					count += 1
					if j != "0":
						f1 = False
						break
				if f1:
					ans = -1
					break
				ans += count - 1
				f = False
				break
	if f:
		ans = -1
				
if (wkans == -1):
	print(ans)
	quit()
if (ans == -1):
	print(wkans)
	quit()
print(min(ans, wkans))

