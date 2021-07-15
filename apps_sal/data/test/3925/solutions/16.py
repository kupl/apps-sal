s=input()
x=len(s)

left=1
for i in range(1,x):
    if s[i]!=s[i-1]:
        left+=1
    else:
        break

right=1
for i in range(x-2,-1,-1):
    if s[i]!=s[i+1]:
        right+=1
    else:
        break

count=1
ANS=0
for i in range(1,x):
    if s[i]!=s[i-1]:
        count+=1

    else:
        if count>ANS:
            ANS=count
        count=1

if count>ANS:
    ANS=count

if left+right>ANS and s[0]!=s[-1]:
    ANS=left+right


print(min(x,ANS))
    

