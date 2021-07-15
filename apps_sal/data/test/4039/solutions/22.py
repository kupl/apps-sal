a,b = map(int,input().split())
A = []
B = []
for i in range(a):
    q,w = map(int,input().split())
    if w<0:
        q = max(q,-w)
        B.append([q+w,q,w])
    else:
        A.append([q,w])
A.sort()
B.sort()
B.reverse()
q = True
i = 0
w = len(A)
while q == True and i<w:
    if b>=A[i][0]:
        b+=A[i][1]
        i+=1
    else:
        q = False
i = 0
w = len(B)
while q == True and i<w:
    if b>=B[i][1]:
        b+=B[i][2]
        i+=1
    else:
        q = False
if q == True and b>=0:
    print('YES')
else:
    print('NO')
