N,X = map(int,input().split())
lsa = [1]
lsp = [1]
for i in range(50):
    lsa.append(2*lsa[-1]+3)
    lsp.append(2*lsp[-1]+1)

def f(n,x):
    if x == 1:
        return 1 if n==0 else 0
    if 1 < x and x <= 1+lsa[n-1]:
        return f(n-1,x-1)
    if x == 2+lsa[n-1]:
        return lsp[n-1]+1
    if 2 + lsa[n-1] < x and x <= 2+2*lsa[n-1]:
        return lsp[n-1]+1+f(n-1,x-2-lsa[n-1])
    if x == 3+2*lsa[n-1]:
        return 2*lsp[n-1] + 1

print(f(N,X))
