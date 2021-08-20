INF = 10 ** 18
(N, K, C) = map(int, input().split())
S = input()
left = [0] * N
right = [0] * N
l = -INF
for i in range(N):
    if S[i] == 'o':
        if l == -INF:
            left[i] = 1
            l = i + C
        elif l < i:
            left[i] = max(left[i], left[i - C - 1] + 1)
            l = i + C
        else:
            left[i] = left[i - 1]
    else:
        left[i] = left[i - 1]
r = INF
for i in reversed(range(N)):
    if S[i] == 'o':
        if r == INF:
            right[i] = 1
            r = i
        elif i < r - C:
            right[i] = max(right[i], right[i + C + 1] + 1)
            r = i
        else:
            right[i] = right[(i + 1) % N]
    else:
        right[i] = right[(i + 1) % N]
for i in range(N):
    lsum = left[i - 1] if i - 1 >= 0 else 0
    rsum = right[i + 1] if i + 1 < N else 0
    if lsum + rsum < K:
        print(i + 1)
