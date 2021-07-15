import sys
s,t =input().split()
a,b = map(int, input().split())
u=input()
if u==s:
    print(a-1,b)
if u==t:
    print(a,b-1)
