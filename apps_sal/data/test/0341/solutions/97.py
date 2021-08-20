(n, k) = list(map(int, input().split()))
(r, s, p) = list(map(int, input().split()))
t = input()
ans = 0
for i in range(k):
    (R, S, P) = (0, 0, 0)
    for hand in t[i::k]:
        if hand == 'r':
            (R, S, P) = (max(S, P), max(R, P), max(R, S) + p)
        elif hand == 's':
            (R, S, P) = (max(S, P) + r, max(R, P), max(R, S))
        elif hand == 'p':
            (R, S, P) = (max(S, P), max(R, P) + s, max(R, S))
    ans += max(R, S, P)
print(ans)
