n = int(input())
s = input().strip()
ans = 0
for i in range(n):
	for j in range(i+1, n+1):
		temp = s[i:j]
		if temp.count('U') == temp.count('D') and temp.count('R') == temp.count('L'):
			ans += 1
print(ans)
