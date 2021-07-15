n , m = map(int,input().split())
que =list(map(int,input().split())) 
auc = list(map(int,input().split()))
s = sum(que)
aa=[]
for i in auc:
    s-=que[i-1]
    aa.append(que[i-1])
aa.sort()
for i in aa[::-1]:
    if i<s:
        s*=2
    else:
        s+=i
print(s)
