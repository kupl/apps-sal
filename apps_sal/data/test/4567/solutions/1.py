n=int(input())
tens=[]
others=[]
for i in range(n):
    s=int(input())
    if s%10==0:
        tens.append(s)
    else:
        others.append(s)
tens.sort(reverse=True)
others.sort(reverse=True)

score=sum(tens)+sum(others)
if score%10==0:
    if len(others)!=0:
        print(score-min(others))
    else:
        print(0)
else:
    print(score)
