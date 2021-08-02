N = int(input())
P = list(map(int, input().split()))
m = P[0]
k = 1
for j in range(N - 1):
    i = j + 1
    if m >= P[i]:
        k += 1
    m = min(m, P[i])
print(k)
