from bisect import bisect_left
A, B, Q = list(map(int, input().split()))
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]

s.sort()
t.sort()

for k in range(Q):
    x = int(input())
    ans = []
    ms = bisect_left(s, x)
    for i in [-1, 0]:
        if 0 <= ms + i <= A - 1:
            mt = bisect_left(t, s[ms + i])
            for j in [-1, 0]:
                if 0 <= mt + j <= B - 1:
                    ans.append(abs(s[ms + i] - x) + abs(t[mt + j] - s[ms + i]))
    mt = bisect_left(t, x)
    for i in [-1, 0]:
        if 0 <= mt + i <= B - 1:
            ms = bisect_left(s, t[mt + i])
            for j in [-1, 0]:
                if 0 <= ms + j <= A - 1:
                    ans.append(abs(t[mt + i] - x) + abs(s[ms + j] - t[mt + i]))
    print((min(ans)))
