st = input()
arr = []
for i in range(len(st)):
	arr.append(st[i:] + st[:i])
arr = sorted(arr)
cnt = 1
for i in range(1,len(st)):
	if(arr[i] != arr[i-1]):
		cnt = cnt + 1
print(cnt)
