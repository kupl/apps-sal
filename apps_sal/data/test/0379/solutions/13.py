n, m = map(int, input().split())
v = []

for i in range(n):
    line = input()
    v.append(line)

u = n
d = 0
l = m
r = 0
    
for i in range(n):
    for j in range(m):
        if v[i][j] == 'X':
            if i < u:
                u = i
            if i > d:
                d = i
            if j < l:
                l = j
            if j > r:
                r = j
                
for i in range(u,d+1):
    for j in range(l, r+1):
        if v[i][j] == ".":
            print("NO")
            return
        
print("YES")
