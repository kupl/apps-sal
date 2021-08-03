n = int(input())
s = [input() for s in range(n)]
m = int(input())
t = [input() for i in range(m)]
plus = []
minus = []
total = []

for i in set(s):
    plus.append(s.count(i))
    minus.append(t.count(i))

for j in range(len(plus)):
    total.append(plus[j] - minus[j])

print(max(0, max(total)))
