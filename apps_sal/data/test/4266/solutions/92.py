k, x = list(map(int, input().split()))

L = []

for i in range(x-k+1, x+k):
    L.append(i)

print((*L))

