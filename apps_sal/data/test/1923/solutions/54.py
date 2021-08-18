N = int(input())
L = list(map(int, input().split()))

L.sort()
L = L[::-1]

r = 0
for i in range(N):
    r += L[1]
    L = L[2:]

print((str(r)))
