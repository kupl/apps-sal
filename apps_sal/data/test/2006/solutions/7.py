(n, m) = list(map(int, input().split()))
d = [0] * m
for i in range(n):
    t = input()
    d[t[t.find('G') + 1:].find('S')] = 1
if d[-1]:
    print(-1)
else:
    print(sum(d))
