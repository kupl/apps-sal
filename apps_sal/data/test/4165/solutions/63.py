N = int(input())
L = list(map(int, input().split()))

length = 0

for i in range(0, N):
    length += L[i]

length -= max(L)

if max(L) < length:
    print('Yes')
else:
    print('No')
