#ARC105 A
import itertools

A, B, C, D = list(map(int,input().split()))
sums = A + B + C + D
lst = [A, B, C, D]

for i in itertools.permutations(lst,1):
    if sum(i) == sums - sum(i):
        print("Yes")
        return
        
for j in itertools.permutations(lst,2):
    if sum(j) == sums - sum(j):
        print("Yes")
        return
        
        
print("No")

