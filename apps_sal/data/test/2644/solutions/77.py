N = int(input())
P = list(map(int, input().split()))
ans = []

idx = [0] * (N + 1)
for n in range(N):
    idx[P[n]] = n

i = 1
while i < N:
    right = idx[i]
    left = i - 1

    if right == left:
        i += 1
    elif right < left:
        break
    else:
        for i in range(right, left, -1):
            P[i], P[i - 1] = P[i - 1], P[i]
            idx[P[i]], idx[P[i - 1]] = idx[P[i - 1]], idx[P[i]]
            ans.append(i)
        i += right - left

check = [n + 1 for n in range(N)]
if P == check and len(ans) == N - 1:
    print(*ans, sep="\n")
else:
    print(-1)
