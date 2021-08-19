import bisect
(A, B, Q) = list(map(int, input().split()))
S = list((int(input()) for _ in range(A)))
T = list((int(input()) for _ in range(B)))
for _ in range(Q):
    x = int(input())
    s = bisect.bisect(S, x)
    t = bisect.bisect(T, x)
    ans = [10 ** 10 * 2] * 4
    if s < A:
        ans[0] = abs(S[s] - x) + min(abs(S[s] - T[max(bisect.bisect(T, S[s]) - 1, 0)]), abs(S[s] - T[min(bisect.bisect(T, S[s]), B - 1)]))
    if s > 0:
        s -= 1
        ans[1] = abs(S[s] - x) + min(abs(S[s] - T[max(bisect.bisect(T, S[s]) - 1, 0)]), abs(S[s] - T[min(bisect.bisect(T, S[s]), B - 1)]))
    if t < B:
        ans[2] = abs(T[t] - x) + min(abs(T[t] - S[max(bisect.bisect(S, T[t]) - 1, 0)]), abs(T[t] - S[min(bisect.bisect(S, T[t]), A - 1)]))
    if t > 0:
        t -= 1
        ans[3] = abs(T[t] - x) + min(abs(T[t] - S[max(bisect.bisect(S, T[t]) - 1, 0)]), abs(T[t] - S[min(bisect.bisect(S, T[t]), A - 1)]))
    print(min(ans))
