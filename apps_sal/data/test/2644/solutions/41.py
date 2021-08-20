N = int(input())
P = list(map(int, input().split()))
P_idx = [0 for _ in range(N)]
for i in range(N):
    P_idx[P[i] - 1] = i
ans = []
i = 0
while i < N:
    idx = P_idx[i]
    if i < idx:
        for j in range(idx - 1, i - 1, -1):
            (P[j], P[j + 1]) = (P[j + 1], P[j])
            ans.append(j + 1)
        i = idx
    else:
        i += 1
check = [i + 1 for i in range(N)]
if P == check and len(ans) == N - 1:
    for i in ans:
        print(i)
else:
    print(-1)
