s=input()
ind=s.find('e')
d=int(s[ind+1:])
z=s.find('.')
a=s[:z]
b=s[z+1:ind]
ans=a
for k in range(d):
    if len(b)<=k:
        ans+='0'
    else:
        ans+=b[k]


if d<len(b):
    ans+='.'
    ans+=b[d:]

i1=ans.find('.')
bo=True
if i1==-1:
    bo=False
    ans1=ans
else:
    ans1=ans[:i1]
    ans2=ans[i1+1:]


def cl1(ans1):

    k=0
    while k<len(ans1)-1:
        
        if ans1[k]!='0':
       
            break
        else:
            ans1=ans1[k+1:]
            
        
    if ans1==None:
        ans1=0
    return ans1


def cl2(ans2):
    for i in range(len(ans2)):
        k=ans2[i:]
        if k.count('0')==len(k):
            ans2=ans2[:i]
            break
    return ans2
if bo:
    
    ans1=cl1(ans1)
    ans2=cl2(ans2)
    total=ans1+'.'+ans2
    if total.endswith('.'):
        print(total[:-1])
    else:
        print(total)
else:
    
    print(cl1(ans1))

