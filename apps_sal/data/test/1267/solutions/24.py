n=int(input())
a=list(map(int,input().split()))
a=list(set(sorted(a)))
cnt=0
if a[0]==0: cnt=-1
cnt+=len(list(a))
print(cnt)
