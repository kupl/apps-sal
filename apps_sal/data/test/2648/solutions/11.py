from collections import Counter

N = int(input())
A = sorted(list(map(int,input().split())))

edible = sum(i-1 for i in Counter(A).values())
print(len(set(A))-edible%2)
