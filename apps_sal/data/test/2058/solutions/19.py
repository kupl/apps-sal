a = input()
b = input()
l = len(b)
p0 = [0] * (l + 1)
s0 = [0] * (l + 1)
p1 = [0] * (l + 1)
s1 = [0] * (l + 1)

for i in range(l):
    if b[i] == '0':
        p1[i + 1] = p1[i] + 1
        p0[i + 1] = p0[i]
    else: 
        p0[i + 1] = p0[i] + 1
        p1[i + 1] = p1[i]
    
for i in range(l - 1, -1, -1):
    if b[i] == '0':
        s1[i] = s1[i + 1] + 1
        s0[i] = s0[i + 1]
    else:
        s0[i] = s0[i + 1] + 1
        s1[i] = s1[i + 1]
    
l1 = len(a)
res = 0
for i in range(l1):
    if a[i] == '0':
        res += p0[l] - p0[i] - s0[l - l1 + i + 1]
    if a[i] == '1':
        res += p1[l] - p1[i] - s1[l - l1 + i + 1]   
print(res)
