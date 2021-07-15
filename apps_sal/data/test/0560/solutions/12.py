S=input
n,m=map(int,S().split())
g=[S() for i in range(n)]
print(n*m-len([1 for i in g if i.count('S')])*len([1 for i in zip(*g) if i.count('S')]))
