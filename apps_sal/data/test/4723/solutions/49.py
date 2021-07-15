#!/bin/python3
s=list(input())
t=list(input())

lens=len(s)
lent=len(t)

for i in reversed(list(range(lens-lent+1))):
  x=s[i:i+lent]
  ans=s
  flag=True
  #print("x",x,len(x))
  for j in range(lent):
    if x[j]!=t[j] and x[j]!="?":
      flag=False
      break
    #if x[j]=="?":
    #  #tと同じ部分
    #  #print("i",i,"j",j)
    #  ans[i+j]=t[j]
  if flag:
    #tより前の部分
    #ans[:i]=["a" if a=="?" else a for a in ans[:i]]
    #tより後ろの部分
    #if i+lent<=lens:
    #  ans[i+lent:lens]=["a" if a=="?" else a for a in ans[i+lent:lens]]
    ans=["a" if a=="?" else a for a in ans[:i]]+\
    	t+["a" if a=="?" else a for a in ans[i+lent:]]
    print(("".join(ans)))
    return
print("UNRESTORABLE")
#print("ans",ans)


