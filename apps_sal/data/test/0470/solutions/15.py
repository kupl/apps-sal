arr = list(map(int, input().split()))
arr.sort()
ans = []
s = sum(arr)
if (len(set(arr)) == len(arr)):
	ans.append(sum(arr))
else:
	if (arr[-1]==arr[-2]==arr[-3]):
		ans.append(arr[0]+arr[1])
	if (arr[-4]==arr[-2]==arr[-3]):
		ans.append(arr[0]+arr[4])
	if (arr[-3]==arr[-4]==arr[-5]):
		ans.append(arr[3]+arr[4])
	for i in range(5):
		for j in range(i + 1, 5):
			if (arr[i] == arr[j]):
				ans.append(s - arr[i] - arr[j])
print(min(ans))
