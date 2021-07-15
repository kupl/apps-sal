s,k=input().split()
k=int(k)
i=-1
count=0
while k>0:
    try:
        if s[i]=='0':
            k-=1
            i-=1
        else:
            i-=1
            count+=1
    except:
        if '0' in s:
            count=len(s)-1
        else:
            count=len(s)
        break
print(count)

