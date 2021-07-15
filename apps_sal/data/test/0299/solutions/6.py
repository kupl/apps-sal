input()
a=list(map(int,input().split()))
d1={1:'chest',2:'biceps',0:'back'}
d2={1:0,2:0,0:0}
for i in range(len(a)):
    d2[(i+1)%3]+=a[i]
Max=0
for i in d2:
    if d2[i]>d2[Max]:
        Max=i
print(d1[Max])
