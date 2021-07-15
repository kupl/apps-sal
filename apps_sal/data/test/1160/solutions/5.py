d = {"S": 0, "M" : 1, "L" : 2, "XL" : 3, "XXL" : 4, "XXXL" : 5}
nums = list(map(int, input().split()))
n = int(input())
ans = ['' for i in range(n)]
no = []
for i in range(n):
	x = input().split(',')
	if len(x) > 1:
		no.append(x + [i])
	else:
		nums[d[x[0]]] -= 1
		ans[i] = x[0]
for i in range(6):
	if nums[i] < 0:
		print("NO")
		return
no.sort(key = lambda x: d[x[0]])
for item in no:
	if nums[d[item[0]]] > 0:
		ans[item[2]] = item[0]
		nums[d[item[0]]] -= 1
	elif nums[d[item[1]]] > 0:
		ans[item[2]] = item[1]
		nums[d[item[1]]] -= 1
	else:
		print("NO")
		return
print("YES")
for i in ans:
	print(i)
