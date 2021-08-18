N, K = map(int, input().split())
R, S, P = map(int, input().split())
p = {"r": P, "s": R, "p": S}

T = [s for s in input()]
ans = 0
for i in range(N):
    if i >= K and T[i] == T[i - K]:
        T[i] = "."
        continue
    ans += p[T[i]]
print(ans)
