(N, X) = map(int, input().split())
L = list(map(int, input().split()))
D = 0
count = 0
for i in range(N + 1):
    if D <= X:
        count += 1
    if i != N:
        D = D + L[i]
print(count)
