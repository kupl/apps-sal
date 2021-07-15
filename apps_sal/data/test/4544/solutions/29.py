import collections
n=int(input())
a=list(map(int,input().split()))
a1=[x-1 for x in a]
a2=[x+1 for x in a]
b=a+a1+a2
c=collections.Counter(b)

print(max(c.values()))
