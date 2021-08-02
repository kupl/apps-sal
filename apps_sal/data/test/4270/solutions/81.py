N = int(input())
V = list(map(int, input().split()))
V.sort()
a = V[0]
for i in range(1, N):
    a = (a + V[i]) / 2
print(a)
