s = [int(j) for j in input().split()]
o = []
for i in range(5):
    if s[i] in s[i+1:]:
        o.append(s[i])
m = sum(s)
for i in o:
    y = 0
    t = 0
    for j in s:
        if j != i or t>2:
            y+=j
        if j == i:
            t+=1
    m = min(y,m)
print(m)
    

