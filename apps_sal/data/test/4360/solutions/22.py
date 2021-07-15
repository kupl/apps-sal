N = int(input())
lsA = list(map(int,input().split()))
d = 0
for i in range(N):
    d += 1/lsA[i]
print(1/d)
