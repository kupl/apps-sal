h,w,d=list(map(int,input().split()))

lis=[[] for i in range(h*w)]
for i in range(h):
  ai=list(map(int,input().split()))
  for j in range(w):
    lis[ai[j]-1].append(i)
    lis[ai[j]-1].append(j)

U=[]

for i in range(d):
  Ui=[0]
  j=1
  while i+j*d<h*w:
    Ui.append(Ui[j-1]+abs(lis[i+j*d][0]-lis[i+(j-1)*d][0])
              +abs(lis[i+j*d][1]-lis[i+(j-1)*d][1]))
    j+=1
  U.append(Ui)

q=int(input())


for i in range(q):
  li,ri=[int(x)-1 for x in input().split()]
  modi=li%d
  print((U[modi][(ri-modi)//d]-U[modi][(li-modi)//d]))

