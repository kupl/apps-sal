n = [int(s) for s in input().split()]
k = int(input())

for i in range(k):
    max_id = n.index(max(n))
    n[max_id] *= 2
print(sum(n)) 
