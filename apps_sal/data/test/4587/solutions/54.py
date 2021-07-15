import bisect
n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
ans=0
for i in b:
    A=bisect.bisect_left(a,i)
    B=len(b)-bisect.bisect_right(c,i)
    ans+=A*B
print(ans)
