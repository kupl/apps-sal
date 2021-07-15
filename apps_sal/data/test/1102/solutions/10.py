n, a = list(map(int, input().split()))
v = list(map(int, input().split()))
a -= 1
it = 0
cnt = 0
while (a - it >= 0) and (a + it < n):
	x = v[a - it] + v[a + it] 
	if it == 0:
		if x == 2:
			cnt += 1
	elif x == 1:
		if it == 0:
			cnt += 1
	elif x == 2:
		cnt += 2
	it += 1

while (a - it >= 0) or (a + it < n):
	if a - it >= 0:
		cnt += v[a - it]
	if a + it < n:
		cnt += v[a + it]
	it += 1

print(cnt)




