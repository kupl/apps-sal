s=input()
n=len(s)
pcnt,gcnt=0,0
ans=[""]*n
for i in range(n):
    if s[i]=="g":
        if gcnt>pcnt:
            ans[i]="p"
            pcnt+=1
        else:
            ans[i]="g"
            gcnt+=1
    if pcnt==n//2 or gcnt==-(-n//2):
        break
i,j=0,0
#print(gcnt,pcnt)
while -(-n//2)>gcnt:
    if ans[i]=="":
        ans[i]="g"
        gcnt+=1
    i+=1
while n//2>pcnt:
    if ans[j]=="":
        ans[j]="p"
        pcnt+=1
    j+=1
score=0
#print(ans)
for i in range(n):
    if ans[i]=="p" and s[i]=="g":
        score+=1
    elif ans[i]=="g" and s[i]=="p":
        score-=1
print(score)
