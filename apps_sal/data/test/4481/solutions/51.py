N = int(input())
S = [input() for _ in range(N)]

d = {s: 0 for s in set(S)}

for i in range(N):
    d[S[i]] += 1

count = 0
for key in d:
    count = max(count, d[key])

l = []
for key in d:
    if count == d[key]:
        l.append(key)
l.sort()

for s in l:
    print(s)
