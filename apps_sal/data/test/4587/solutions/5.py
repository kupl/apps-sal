import bisect
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
a=sorted(A)
b=sorted(B)
c=sorted(C)
ans=0
for i in range(len(b)):
    index_a=bisect.bisect_left(a,b[i])
    index_c=bisect.bisect_right(c,b[i])
    ans+=(index_a*(len(c)-index_c))
print(ans)
