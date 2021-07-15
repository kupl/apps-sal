n = int(input())
s = input()
res = 1

for i in range(0, n - 1):
	if s[i] != s[i + 1]: res += 1
	
print(min(res + 2, n))

