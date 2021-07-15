s = input().split()
n = int(s[0])
m = int(s[1])
a = []
b = []
down = []
up = []
for i in range(n):
    a.append(input())
for i in range(m):
    for j in range(n):
        if a[j][i] == '*':
            b.append(n-j)
            break

for i in range(len(b)-1):
    if b[i] <= b[i+1]:
        up.append(b[i+1]-b[i])
    else:
        down.append(b[i] - b[i+1])
if len(down) == 0:
    down.append(0)
if len(up) == 0:
    up.append(0)
print(max(up), max(down))
        

