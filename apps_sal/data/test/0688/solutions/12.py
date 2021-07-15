s1=input()
s2=input()
n=len(s1)
m=len(s2)
from collections import Counter 
c1=Counter(s1)
c2=Counter(s2)
if c1['2'] and c1['5']:
    tot=c2['2']+c2['5']
    a=c1['2']
    b=c1['5']
    c=a+b
    have2=a/c*tot 
    have5=b/c*tot 
elif c1['2'] or c1['5']:
    have2=have5=c2['2']+c2['5']
if c1['6'] and c1['9']:
    tot=c2['6']+c2['9']
    a=c1['6']
    b=c1['9']
    c=a+b 
    have6=a/c*tot 
    have9=b/c*tot 
elif c1['6'] or c1['9']:
    have6=have9=c2['6']+c2['9']
mini=10**9 
for i in c1.keys():
    if i not in "2569" and c1[i]:
        mini=min(mini,c2[i]//c1[i]) 
if c1['2'] :
    mini=min(mini,have2//c1['2'])
if c1['5']:
    mini=min(mini,have5//c1['5'])
if c1['6'] :
    mini=min(mini,have6//c1['6'])
if c1['9']:
    mini=min(mini,have9//c1['9'])
mini=int(mini)
print(mini if mini!=10**9 else 0 )
