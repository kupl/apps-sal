N, M = list(map(int, input().split()))
K1 = []
for i in range(N):
    K1.append(list(map(int, input().split())))

new_K1 = []
for n in range(N):
    del K1[n][0]
    new_K1.extend(K1[n])

count = 0
for y in range(1, M + 1):
    if new_K1.count(y) == N:
        count += 1

print(count)
