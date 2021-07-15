n = int(input())
a = int(input())
b = int(input())
c = int(input())

ans = 0

if n == 1:
	pass
elif n == 2:
	ans += min(a, b)
else:
	if c < a and c < b:
		ans += min(a, b) + (n - 2) * c
	else:
		ans += (n - 1) * min(a, b)

print(ans)
