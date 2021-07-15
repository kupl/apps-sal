n = int(input())
al = list(map(int, input().split()))
bl = [0]*(n+1)
cl = [0]*(n-1)

for i in range(n):
    bl[i+1] = al[i] + bl[i]

for j in range(1, n):
    cl[j-1] = abs(bl[j] - (bl[n] - bl[j]))

print(min(cl))
