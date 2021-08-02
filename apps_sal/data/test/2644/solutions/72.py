def int_1(n):
    return int(n) - 1


N = int(input())
P = list(map(int_1, input().split()))

Number = [0] * N
for idx, p in enumerate(P):
    Number[p] = idx

ans = []
target = 0
start = 0
while True:
    target_idx = Number[target]
    if target_idx <= start:
        print((-1))
        return
    for idx in range(target_idx - 1, start - 1, -1):
        P[idx + 1], P[idx] = P[idx], P[idx + 1]
        ans.append(idx)
    target = target_idx
    start = target_idx
    if start == N - 1:
        break
for idx, p in enumerate(P):
    if p != idx:
        print((-1))
        return
for an in ans:
    print((an + 1))
