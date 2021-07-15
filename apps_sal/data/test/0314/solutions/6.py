n,k = list(map(int, input().split()))
A = list(map(int, input().split()))

arya = 0
bran = 0

for i,a in enumerate(A):
    arya += a 
    bran += min(arya, 8)
    arya -= min(arya, 8)
    if bran >= k:
        print(i+1)
        return

print(-1)

