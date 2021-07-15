class letter(object):
    def __init__(self,let,val):
        self.let=let
        self.val=val

    def __lt__(self,other):
        return self.val<other.val

n=int(input())
s=input()
candi=[[] for i in range(n//2)]
ans=0
for i,vl in enumerate(map(int,input().split())):
    candi[min(i,n-i-1)].append((letter)(s[i],vl))
    ans+=vl
for i in range(n//2):
    candi[i].sort()
ti=[0 for i in range(26)]
sum=0
for i in range(n//2):
    if candi[i][0].let==candi[i][1].let:
        ans-=candi[i][0].val
        ti[ord(candi[i][0].let)-ord('a')]+=1
        sum+=1

mx=0
p=0
for i in range(26):
    if ti[i]>mx:
        mx=ti[i]
        p=i
b=[]
for i in range(n//2):
    if ord(candi[i][0].let)-ord('a')!=p and ord(candi[i][1].let)-ord('a')!=p and candi[i][0].let!=candi[i][1].let:
        b.append(candi[i][0])
b.sort()
i=0
while mx*2>sum:
    sum+=1
    ans-=b[i].val
    i+=1
print(ans)
