import sys
n = int(input())
s = input()
k = (n - 11) // 2
licz = 0
for i in range(n):
	if s[i] == '8':
		licz += 1
if licz <= k:
	print("NO")
	return
licz = 0
i = -1
while True:
	i += 1
	if s[i] == '8':
		licz += 1
	if licz == k + 1:
		break
if i > 2 * k:
	print("NO")
else:
	print("YES")
