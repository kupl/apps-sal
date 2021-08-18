N = int(input())
a = list(map(int, input().split()))

L = {}

for i in range(N):
    L[i] = a[i]

sort_L = sorted(L.items(), key=lambda x: x[1])

for j in sort_L:
    print(j[0] + 1, end=" ")
