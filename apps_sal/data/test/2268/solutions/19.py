inp = input().strip().split()
n, m = int(inp[0]), int(inp[1])
s = input().strip()
d = {}
for i in range(n):
    if(s[i] in d):
        d[s[i]].append(i)
    else:
        d[s[i]] = [i]

for i in range(m):
    inp = input().strip().split()
    l0, l1 = [], []
    b0, b1 = False, False
    if(inp[0] in d):
        # l0=d[inp[0]]
        b0 = True
    if(inp[1] in d):
        # l1=d[inp[1]]
        b1 = True
    if(b0 and b1):
        d[inp[0]], d[inp[1]] = d[inp[1]], d[inp[0]]
    elif(b0 and (not b1)):
        d[inp[1]] = d[inp[0]]
        del(d[inp[0]])
    elif(b1 and (not b0)):
        d[inp[0]] = d[inp[1]]
        del(d[inp[1]])


ans = [0] * n
for key in d.keys():
    for i in d[key]:
        ans[i] = key

for ctmp in ans:
    print(ctmp, end='')
print()
