X=int(input())

p=[True for _ in range(0,200000+1)]
p[0]=False
p[1]=False
for i in range(2,200000+1):
    if p[i]==False:
        continue
    for j in range(2,200000//i):
        p[i*j]=False

while p[X]==False:
    X+=1
print(X)

