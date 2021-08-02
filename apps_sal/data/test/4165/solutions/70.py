N = int(input())
L = list(map(int, input().split()))

m = max(L)
s = sum(L) - m

if m < s: print('Yes')
else: print('No')
