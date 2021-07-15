import itertools
def II(): return int(input())
def LII(): return tuple(map(int, input().split()))

n=II()
p=LII()
q=LII()

seq = list(itertools.permutations([i for i in range(1,n+1)]))

result=abs(seq.index(p)-seq.index(q))
print(result)

