from collections import defaultdict

n, k = [int(i) for i in input().split()]

x = []
v = defaultdict(int)
for i in range(n):
    v[int(input())] += 1
a = 0

for i in v.values():
    a += i // 2

print(2 * a + (((n + 1) // 2) - a))
