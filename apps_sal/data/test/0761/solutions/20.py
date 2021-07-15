n = int(input())
a = list(map(int, input().split()))

if n == 1:
	print(sum(a))
	return

mn = min(a)
mx = max(a)
s = 0

for i in a:
	s += abs(i)

print(s - abs(mn) - abs(mx) + mx - mn)
