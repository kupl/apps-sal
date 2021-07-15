import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

#bit全部作ってる
#bit = [i>>j&1 for j in range(N)]

n,m=MI()
lights=[LI() for _ in range(m)]
p_list=LI()

bit_list=[]
count=0
for i in range(2**n):
    bit = [i>>j&1 for j in range(n)]
    flag=0
    for j in range(m):
        ki=lights[j][0]
        onswitch=0
        for k in range(1,ki+1):
            si=lights[j][k]
            onswitch+=bit[si-1]
        if onswitch%2!=p_list[j]:
            flag+=1
    if flag==0:
        count+=1
print(count)
