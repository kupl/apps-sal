import bisect
(A, B, Q) = map(int, input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
S = sorted(S)
T = sorted(T)
for j in range(Q):
    x = int(input())
    a = S[bisect.bisect_left(S, x) - 1]
    b = T[bisect.bisect_left(T, x) - 1]
    if x <= S[-1]:
        a_ = S[bisect.bisect_right(S, x)]
    else:
        a_ = S[bisect.bisect_right(S, x) - 1]
    if x <= T[-1]:
        b_ = T[bisect.bisect_right(T, x)]
    else:
        b_ = T[bisect.bisect_right(T, x) - 1]
    y = min([abs(a - x) + abs(b - a), abs(a - x) + abs(b_ - a), abs(a_ - x) + abs(b - a_), abs(a_ - x) + abs(b_ - a_), abs(b - x) + abs(a - b), abs(b - x) + abs(a_ - b), abs(b_ - x) + abs(a - b_), abs(b_ - x) + abs(b_ - a_)])
    print(y)
