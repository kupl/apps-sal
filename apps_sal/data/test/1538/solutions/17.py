from collections import Counter
n=int(input())
li=input().strip().split(' ')
print(max(Counter(li).values()))
