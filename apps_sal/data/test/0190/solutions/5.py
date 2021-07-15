s = input().split()
n = int(s[0])
m = int(s[1])
a = []
b = []
c = []
d = []
for i in range(n):
    a.append(input())
for j in range(m):
    for i in range(n):
        if a[i][j] == '*':
            b.append(i)

c.append(max(b) - min(b)+1)
b = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            b.append(j)
d.append(max(b) - min(b)+1)
print(max(max(c),max(d)))






















    

