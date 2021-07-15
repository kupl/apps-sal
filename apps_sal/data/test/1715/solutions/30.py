import bisect
a, b, q = list(map(int, input().split()))

s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]

s.append(-100000000000)
s.append(100000000000)
t.append(-100000000000)
t.append(100000000000)
s.sort()
t.sort()

for _ in range(q):
    x = int(input())

    idxs = bisect.bisect_right(s, x)
    idxt = bisect.bisect_right(t, x)
    left_s = s[idxs - 1]
    right_s = s[idxs]
    left_t = t[idxt - 1]
    right_t = t[idxt]

    kouho1 = max(x - left_s, x - left_t)
    kouho2 = max(right_s - x, right_t - x)
    kouho3 = min(x - left_s, right_t - x) * 2 + max(x - left_s, right_t - x)
    kouho4 = min(x - left_t, right_s - x) * 2 + max(x - left_t, right_s - x)
    print((min(kouho1, kouho2, kouho3, kouho4)))

