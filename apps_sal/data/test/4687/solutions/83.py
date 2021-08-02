N, K = list(map(int, input().split()))

ab = [[0, 0]] * N
for i in range(N):
    _a, _b = list(map(int, input().split()))
    ab[i] = [_a, _b]
ab.sort(key=lambda x: x[0])


total = 0
for pair in ab:
    total += pair[1]
    if total >= K:
        print((pair[0]))
        break
