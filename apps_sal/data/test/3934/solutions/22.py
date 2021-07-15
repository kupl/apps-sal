n = int(input())
counts = [0] * n

for _ in range(n-1):
	u, v = map(int, input().split())
	u -= 1
	v -= 1
	counts[u] += 1
	counts[v] += 1

all_possible = all(count != 2 for count in counts)

if all_possible:
	print("YES")
else:
	print("NO")
