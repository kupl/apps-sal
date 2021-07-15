
n = int(input())
p1=['0' for _ in range(n)]
p2=['0' for _ in range(n)]
t1=[]
t2=[]
for i in range(n):
    a, b = map(int, input().split())
    t1.append((a,i))
    t2.append((b,i))
t2.sort()
t1.sort()
for k in range((n//2)):
    p1[t1[k][1]]='1'
    p2[t2[k][1]]='1'
i=0
j=0
for k in range(n):
    if t1[i][0]<t2[j][0]:
        p1[t1[i][1]]='1'
        i+=1
    else:
        p2[t2[j][1]]='1'
        j+=1

print("".join(p1))
print("".join(p2))
