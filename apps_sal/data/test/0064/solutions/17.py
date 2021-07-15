from collections import Counter as cc
n,m=list(map(int,input().split()))
s=[i for i in input()]
c=cc(s)
if max(c.values())>m:
    print("NO")
else:
    print("YES")

