import itertools

n = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

p_num = 0
q_num = 0

for i,s in enumerate(itertools.permutations([i for i in range(1,n+1)])):
    if len([x for x,y in zip(s,p) if x==y]) == n:
        p_num = i
    if len([x for x,y in zip(s,q) if x==y]) == n:
        q_num = i
print(abs(p_num-q_num))
