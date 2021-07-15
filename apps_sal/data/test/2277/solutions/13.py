from sys import stdin

n = int(stdin.readline())
a = [int(o) for o in stdin.readline().split()]

inv = len([ 1 for i in range(n) for j in range(i + 1, n) if a[i] > a[j]])
ans = inv % 2

m = int(stdin.readline())

output = []

for i in range(m):
	l, r = map(int, stdin.readline().split())

	v = ((r - l + 1) * (r - l) // 2) % 2
	ans ^= v

	if ans == 0:
		output.append("even")

	else: output.append("odd")

print('\n'.join(output))
