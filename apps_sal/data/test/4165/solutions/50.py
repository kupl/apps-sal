N = int(input())
L = list(map(int, input().split()))
m = max(L)
L.pop(L.index(max(L)))
if m < sum(L):
    print('Yes')
else:
    print('No')
