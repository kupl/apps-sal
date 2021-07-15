n = int(input())
s1 = [int(x) for x in input()]
s2 = [int(x) for x in input()]

def min(a, b):
	if a < b:
		return a
	else:
		return b

ans = 0
for i in range(n):
	abso = abs(s1[i] - s2[i])
	ans += min(abso, 10 - abso)
	
print(ans)
