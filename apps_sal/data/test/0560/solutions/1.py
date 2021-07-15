r,c=input().split()
r=int(r)
c=int(c)
rows=[]
evils=0
for i in range(r):
    rows.append(input())
    evils+=rows[-1].count('S')
eaten=(r*c)-evils
columns=[]
for i in range(c):
    L=[]
    for j in range(r):
        L.append(rows[j][i])
    columns.append(L)

for i in range(r):
    for j in range(c):
        if(rows[i][j]=='S'):
            continue
        elif('S' in rows[i] and 'S' in columns[j]):            
            eaten-=1
print(eaten)



