N, K = list(map(int, input().split()))

ab = [[0, 0]] * N
for i in range(N):
    _a, _b = list(map(int, input().split()))
    ab[i] = [_a, _b]
ab.sort(key=lambda x:x[0])

j = 0
index = 0
while j < K:
    j += ab[index][1]
    if j < K:
        index += 1

print((ab[index][0]))

