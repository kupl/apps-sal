n, L = map(int, input().split())

if n == 1:
	print('YES')
	return

first = list(map(int, input().split()))
second = list(map(int, input().split()))

def shift(lst, value):
	for i in range(len(lst)):
		lst[i] -= value
	return lst

def equal(lst1, lst2):
	for i in range(len(lst1)):
		if lst1[i] != lst2[i]:
			return False
	return True

first = shift(first, first[0])
second = shift(second, second[0])

for i in range(n):
	first = shift(first, first[1])
	first = first[1:] + [L + first[0]]
	if equal(first, second):
		print("YES")
		return

print('NO')
