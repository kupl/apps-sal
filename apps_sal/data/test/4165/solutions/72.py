N = int(input())
L = list(map(int, input().split()))

M = max(L)
m = L.index(M)
s = sum(L[:m]) + sum(L[m+1:])

if M < s: print('Yes')
else: print('No')
