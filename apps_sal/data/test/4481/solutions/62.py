n = int(input())
s = [input() for _ in range(n)]
ans = []
d = {}
for i in s:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1
mx = 0
for value in list(d.values()):
    if value > mx:
        mx = value
for (key, value) in list(d.items()):
    if value == mx:
        ans.append(key)
for v in sorted(ans):
    print(v)
