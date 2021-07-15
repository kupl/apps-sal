import sys
input()
t=list(map(int,input().split()))
s=[2000000 for i in range(200001)]
for i in range(len(t)):
    s[t[i]]=i
mins=2000001
mn=0
for i in range(len(s)):
    if s[i]<mins:
        mins=s[i]
        mn=i
print(mn)

