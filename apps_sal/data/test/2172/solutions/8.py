# B

l = input().split()
n = int(l[0])
m = int(l[1])
x = []
y = []
for i in range(m):
    inp = input().split()
    x.append(inp[0])
    if len(inp[1])<len(inp[0]):
        y.append(inp[1])
    else:
        y.append(inp[0])
prof = input().split()
for i in range(n):
    prof[i] = y[x.index(prof[i])]
    
s = prof[0]
for i in range(1,n):
    s += ' '+prof[i]

print(s)

