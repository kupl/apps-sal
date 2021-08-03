N = int(input())
d = dict()
for _ in range(N):
    S = input()
    if S not in d:
        d[S] = 0
    d[S] += 1
M = max(d.values())
ans = []
for S in list(d.keys()):
    if d[S] == M:
        ans.append(S)
ans.sort()
for S in ans:
    print(S)
