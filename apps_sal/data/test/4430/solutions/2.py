n,m,k = list(map(int, input().split()))
list_a = list(map(int, input().split()))
list_a.reverse()
count_b = 0
sum_now = 0
ans = 0
i = 0
while i < n:
	if count_b >= m:
		ans = i - 1
		break
	sum_now += list_a[i]
	if sum_now > k:
		sum_now = 0
		count_b +=1
	else:
		i += 1
else:
	ans = n-1
print(ans+1)

