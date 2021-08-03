N = int(input())
P = list(enumerate(list(map(int, input().split()))))
P = sorted(P, key=lambda x: x[1])

before_idx = list(range(-1, N - 1)) + [-1, -1]
next_idx = list(range(1, N + 1)) + [N, N]
ans = 0
for i, p in P:
    il1 = before_idx[i]
    il2 = before_idx[il1]
    ir1 = next_idx[i]
    ir2 = next_idx[ir1]
    ans += p * ((i - il1) * (ir2 - ir1) + (ir1 - i) * (il1 - il2))
    before_idx[ir1] = il1
    next_idx[il1] = ir1


print(ans)
