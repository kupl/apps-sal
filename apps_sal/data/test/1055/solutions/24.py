n = int(input())
a = list(map(int, input().split()))


def sort_(a):
	mid = len(a) // 2
	if sorted(a) == a:
		return len(a)
	else:
		return max(sort_(a[:mid]), sort_(a[mid:]))

print(sort_(a))
