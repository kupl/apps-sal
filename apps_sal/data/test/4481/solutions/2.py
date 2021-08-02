n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
mx = max(d.values())
ans = ['']
for k, v in d.items():
    if v == mx:
        ans.append(k)
ans.sort()
print(*ans, sep='\n')
