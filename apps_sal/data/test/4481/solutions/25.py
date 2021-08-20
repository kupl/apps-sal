N = int(input())
d = {}
for i in range(N):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
l = sorted(d.items())
M = max(d.values())
for i in l:
    if d[i[0]] == M:
        print(i[0])
