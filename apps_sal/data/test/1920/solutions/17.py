n = int(input())
day = [[0, 0] for i in range(368)]
for i in range(n):
	a, b, c = (input().split())
	if(a == "M"):
		day[int(b)][0] += 1
		day[int(c)+1][0] -= 1
	else:
		day[int(b)][1] += 1
		day[int(c)+1][1] -= 1

w = 0
m = 0
ans = 0
for i in day:
	w += i[0]
	m += i[1]
	ans = max(2 * min(m, w), ans)
print(ans)
