from collections import Counter
n = int(input())
s = input().strip()[:n]
t = input().strip()[:n]
if Counter(s) != Counter(t):
    print(-1)
    return

res = []
for i in range(n):
    pos = s[i:].find(t[i])
    for k in range(i+pos, i, -1):
        res.append(k)
    # print(s)
    s = s[i+pos] + s[:i+pos]  + s[i+pos +1 :]
print(len(res))
print(*res)

