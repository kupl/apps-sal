from collections import Counter
import sys

N=int(input())
cards=list(map(int,sys.stdin.readline().strip().split()))
c=Counter(cards)

even=len([x for x in iter(c) if c[x]%2==0])
odd=len([x for x in iter(c) if c[x]%2==1])

print(even-(even%2)+odd)
