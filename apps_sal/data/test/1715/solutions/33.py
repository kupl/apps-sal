from bisect import bisect_left
(A, B, Q) = map(int, input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
for i in range(Q):
    x = int(input())
    si = bisect_left(S, x)
    ti = bisect_left(T, x)
    if 0 < si < A and 0 < ti < B:
        (sl, sr) = (abs(x - S[si - 1]), abs(x - S[si]))
        (tl, tr) = (abs(x - T[ti - 1]), abs(x - T[ti]))
        print(min(max(sr, tr), max(sl, tl), sl + tr + min(sl, tr), sr + tl + min(sr, tl)))
    elif si == 0 and ti == 0:
        sr = abs(x - S[si])
        tr = abs(x - T[ti])
        print(max(sr, tr))
    elif si == A and ti == B:
        sl = abs(x - S[si - 1])
        tl = abs(x - T[ti - 1])
        print(max(sl, tl))
    elif si == 0 and ti == B:
        sr = abs(x - S[si])
        tl = abs(x - T[ti - 1])
        print(sr + tl + min(sr, tl))
    elif si == A and ti == 0:
        sl = abs(x - S[si - 1])
        tr = abs(x - T[ti])
        print(sl + tr + min(sl, tr))
    elif si == 0:
        sr = abs(x - S[si])
        (tl, tr) = (abs(x - T[ti - 1]), abs(x - T[ti]))
        print(min(max(sr, tr), sr + tl + min(sr, tl)))
    elif si == A:
        sl = abs(x - S[si - 1])
        (tl, tr) = (abs(x - T[ti - 1]), abs(x - T[ti]))
        print(min(max(sl, tl), sl + tr + min(sl, tr)))
    elif ti == 0:
        (sl, sr) = (abs(x - S[si - 1]), abs(x - S[si]))
        tr = abs(x - T[ti])
        print(min(max(sr, tr), sl + tr + min(sl, tr)))
    elif ti == B:
        (sl, sr) = (abs(x - S[si - 1]), abs(x - S[si]))
        tl = abs(x - T[ti - 1])
        print(min(max(sl, tl), sr + tl + min(sr, tl)))
