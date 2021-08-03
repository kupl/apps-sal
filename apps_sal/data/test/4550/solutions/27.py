L = list(map(int, input().split()))
L.sort()
print('Yes' if sum(L[:2]) == L[2] else 'No')
