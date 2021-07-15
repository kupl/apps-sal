n, b, p = list(map(int, input().split(" ")))
dup = n
ans = 0
while n>1:
	ans += (n//2)*(2*b + 1)
	n = n//2 + n%2
print(ans, p*dup)
