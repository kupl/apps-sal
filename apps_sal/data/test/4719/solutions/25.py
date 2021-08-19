from collections import Counter
n = int(input())
cl = {chr(i): 0 for i in range(97, 123)}
s = input()
for k in Counter(s).keys():
    cl[k] = Counter(s)[k]
for i in range(n - 1):
    s = input()
    for k in cl.keys():
        if cl[k] != 0:
            cl[k] = min(cl[k], Counter(s).get(k, 0))
ans = []
for (k, v) in cl.items():
    if v != 0:
        for i in range(v):
            ans.append(k)
print(''.join(sorted(ans)))
