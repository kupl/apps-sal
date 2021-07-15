f = open("input.txt","r")
n, k = map(str,f.readline().split())
f1 = open("output.txt","w")
n = int(n); k = int(k)
b = []; c = []
a = list(map(str,f.readline().split()))
for i in range(len(a)): a[i] = int(a[i])
p = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] <= a[j] and i != j: p += 1
    if p >= k-1: b.append(a[i])
    p = 0
f1.write(str(max(b)))
p = 0
c.append(a.index(max(b))+1)
for i in range(len(a)):
    if a[i] >= max(b) and p < k-1 and i+1 not in c:
        c.append(i+1); p += 1
c.sort()
f1.write("\n")
for i in range(len(c)): f1.write(str(c[i])); f1.write(" ")
f.close(); f1.close()
