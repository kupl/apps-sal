n,m=map(int,input().split())
s=[]
st=set()
cst=set()
for i in range(n):
    s.append(input())
    for j in range(len(s[i])):
        if s[i][j]=='#':
            st.add((i,j))
for i in range(1,n-1):
    for j in range(1,m-1):
        if s[i-1][j-1]!='#':
            continue
        if s[i - 1][j ] != '#':
            continue
        if s[i-1][j+1]!='#':
            continue
        if s[i][j-1]!='#':
            continue
        if s[i][j+1]!='#':
            continue
        if s[i+1][j-1]!='#':
            continue
        if s[i+1][j]!='#':
            continue
        if s[i+1][j+1]!='#':
            continue
        cst.add((i-1,j))
        cst.add((i - 1, j-1))
        cst.add((i - 1, j+1))
        cst.add((i + 1, j))
        cst.add((i + 1, j-1))
        cst.add((i + 1, j+1))
        cst.add((i , j+1))
        cst.add((i , j-1))
if len(cst)==len(st):
    print('YES')
else:
    print('NO')
