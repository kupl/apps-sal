n, k = map(int, input().split())
arr = list(map(int, input().split()))
lol = {}
flag = {}
arr.sort()

for x in arr:
	flag[x] = 1

ans = 0
for i in range(len(arr)):
	if arr[i] in lol:
		continue
	
	cur = arr[i]
	cnt = 0

	while cur <= 1000000000:
		lol[cur] = 1
		if cur in flag:
			cnt += 1
		else:
			break
		cur = cur * k
		if k == 1:
			break

	ans += (cnt + 1) // 2
print(ans)
