import itertools
n=int(input());p,a,b=sorted(itertools.permutations(range(1,n+1),n)),[*map(int,input().split())],[*map(int,input().split())]
print(abs(([list(i)==a for i in p].index(True)+1)-([list(i)==b for i in p].index(True)+1)))
