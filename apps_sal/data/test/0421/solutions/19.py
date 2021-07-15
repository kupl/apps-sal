cin = lambda:map(int,input().split())
n, = cin()
a=[]
count=1
for i in range(0,n):
       a.append(tuple(list(cin())[::-1]))
a.sort()   
ref = a[0][0]
for i in range(1,len(a)):
    if a[i][1]>ref:
        count+=1
        ref=a[i][0] 
print(count)
