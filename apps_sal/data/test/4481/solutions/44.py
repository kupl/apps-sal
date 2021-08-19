N = int(input())
d = {}
for _ in range(N):
    s = input()
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1
max_n = max(d.values())
ans = []
for (key, value) in d.items():
    if value == max_n:
        ans.append(key)
ans.sort()
for i in ans:
    print(i)
