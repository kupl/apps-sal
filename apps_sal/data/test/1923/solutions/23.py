N = int(input())
L = [int(i) for i in input().split()]
L.sort(reverse=True)
S = 0
for i in range(N):
    S += L[2 * i + 1]
print(S)
