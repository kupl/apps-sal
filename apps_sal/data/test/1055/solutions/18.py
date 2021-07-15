n = int(input())
a = list(map(int, input().split()))
def check(x):
	if x != sorted(x):
		return max(check(x[:len(x) // 2]), check(x[len(x) // 2:]))
	return len(x)
print(check(a))
