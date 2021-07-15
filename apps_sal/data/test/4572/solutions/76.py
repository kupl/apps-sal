S=input()
X=set([s for s in 'abcdefghijklmnopqrstuvwxyz'])
for s in S:
  X.discard(s)
X=list(X)
X.sort()
X.append('None')
print(X[0])
