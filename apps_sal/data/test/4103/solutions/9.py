import sys
input = sys.stdin.readline

n,b,a=list(map(int,input().split()))
S=list(map(int,input().split()))

bn=b
an=a

for i in range(n):
    #print(bn,an)
    if bn==0 and an==0:
        print(i)
        return
    if S[i]==1 and bn>0 and an<a:
        bn-=1
        an+=1
    elif an>0:
        an-=1
    else:
        bn-=1

print(n)


