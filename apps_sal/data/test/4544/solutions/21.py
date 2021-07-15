from collections import Counter

n=int(input())
l=list(map(int,input().split()))

a=[i-1 for i in l]
b=[i+1 for i in l]

l=Counter(l+a+b)

print(l.most_common()[0][1])
