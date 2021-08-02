n = int(input())
c = {}
for i in range(n):
    c[i] = []
for i in range(n - 1):
    c[int(input()) - 1].append(i + 1)
f = True
for i in range(n):
    cl = 0
    for j in c[i]:
        if len(c[j]) == 0: cl += 1
    if len(c[i]) != 0 and cl < 3: f = False
print('Yes' if f else 'No')
