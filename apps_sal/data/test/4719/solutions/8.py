n = int(input())
S = [input() for _ in range(n)]
alp = 'abcdefghijklmnopqrstuvwxyz'
count = [float('inf') for _ in range(len(alp))]
for s in S:
    for i in range(len(alp)):
        count[i] = min(count[i], s.count(alp[i]))
ans = ''
for i in range(len(alp)):
    ans += alp[i] * count[i]
print(ans)
