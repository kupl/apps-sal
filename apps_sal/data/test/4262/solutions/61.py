import itertools

n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))

dict=list(itertools.permutations(list(range(1,n+1))))
print((abs(dict.index(p)-dict.index(q))))

