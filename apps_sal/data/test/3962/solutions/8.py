import sys
lines = sys.stdin.readlines()
n = int(lines[0])
l = list()
r = list()
lines = lines[1:]
for i in range(n):
    words = lines[i].split(' ')
    l.append(int(words[0]))
    r.append(int(words[1]))
l.sort()
r.sort()
ans = 0
for i in range(n):
    ans += max(l[i], r[i])
ans += n
print(ans)
