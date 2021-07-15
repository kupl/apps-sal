n = int(input())
a = [0 for _ in range(26)]

for _ in range(n):
	name = input()
	a[ord(name[0]) - ord('a')] += 1

t = 0
for m in a:
	l1 = m // 2
	l2 = m - l1

	t += l1 * (l1 - 1) // 2
	t += l2 * (l2 - 1) // 2
print(t)
