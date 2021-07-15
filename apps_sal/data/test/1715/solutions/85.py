import bisect
A, B, Q = map(int, input().split())
s = list(int(input()) for _ in range(A))
t = list(int(input()) for _ in range(B))

for i in range(Q):
    ans = 10 ** 19
    x = int(input())
    stmp1 = bisect.bisect_left(s, x)
    for j in range(2):
        if stmp1 == 0 and j == 1:
            continue
        if stmp1 == A and j == 0:
            continue
        ttmp1 = bisect.bisect_left(t, s[stmp1 - j])
        ktmp = 10 ** 11
        if ttmp1 != 0:
            ktmp = min(ktmp, abs(s[stmp1 - j] - t[ttmp1 - 1]))
        if ttmp1 != B:
            ktmp = min(ktmp, abs(s[stmp1 - j] - t[ttmp1]))
        total = abs(x - s[stmp1 - j]) + ktmp
        ans = min(ans, total)

    ttmp1 = bisect.bisect_left(t, x)
    for j in range(2):
        if ttmp1 == 0 and j == 1:
            continue
        if ttmp1 == B and j == 0:
            continue
        stmp1 = bisect.bisect_left(s, t[ttmp1 - j])
        ktmp = 10 ** 11
        if stmp1 != 0:
            ktmp = min(ktmp, abs(t[ttmp1 - j] - s[stmp1 - 1]))
        if stmp1 != A:
            ktmp = min(ktmp, abs(t[ttmp1 - j] - s[stmp1]))
        total = abs(x - t[ttmp1 - j]) + ktmp
        ans = min(ans, total)
    print(ans)
