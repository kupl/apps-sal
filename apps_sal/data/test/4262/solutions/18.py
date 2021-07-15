N,P,Q=open(0);*P,=map(int,P.split());*Q,=map(int,Q.split())
f=lambda i:i*f(i-1)if i else 1
g=lambda l:(l[0]-1)*f(len(l)-1)+g([e-1if e>l[0]else e for e in l[1:]])if l else 0
print(abs(g(P)-g(Q)))
