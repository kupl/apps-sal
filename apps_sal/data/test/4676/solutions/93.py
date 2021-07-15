O = list(input())
lo = len(O)
E = list(input())
le = len(E)
w = lo + le

X = ['*']*w
for i in range(le):
  X[2*i] =O[i]
  X[2*i+1] = E[i]
if lo > le:
  X[-1] = O[-1]
  
print(''.join(X))
