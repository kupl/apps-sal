n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
li = []
for i in range(n):
    li += [s.count(s[i]) - t.count(s[i])]
print(max(max(li), 0))
