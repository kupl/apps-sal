from collections import defaultdict
d = defaultdict(int)
for _ in range(int(input())):
    d[input()] += 1
for _ in range(int(input())):
    d[input()] -= 1
print(max(0, max(d.values())))
