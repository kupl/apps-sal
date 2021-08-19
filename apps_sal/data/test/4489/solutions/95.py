n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
k = set(s)
tot = 0
for i in k:
    tot = max(s.count(i) - t.count(i), tot)
print(tot)
