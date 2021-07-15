import sys

s=input()
k=int(input())


s=list(s)

c=0
for i in range(len(s)):
        if s[i]=='1':
                c+=1
if c==len(s):
        print('1')
        return

d=0
if len(s)>=k:
        for i in range(k):
                if s[i]=='1':
                        d+=1
if d==k:
        print('1')
        return

for i in range(len(s)):
        if s[i]!='1':
                print(s[i])
                return
