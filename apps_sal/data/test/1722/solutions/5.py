from collections import defaultdict
n = int(input())
c = defaultdict(int)
for _ in range(n):
    name = input()
    c[name[0]] += 1
total = 0
for k, v in c.items():
    left = v // 2
    right = (v + 1) // 2
    total += (left * (left - 1)) // 2
    total += (right * (right - 1)) // 2
print(total)
