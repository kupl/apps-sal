(h, m) = list(map(int, input().split()))
(H, D, C, N) = list(map(int, input().split()))
after = C * 0.8
ans = (H + N - 1) // N * C
tm = h * 60 + m
tm1 = 20 * 60 + 0
tm2 = 23 * 60 + 59
if tm1 <= tm <= tm2:
    print('{:.16f}'.format((H + N - 1) // N * after))
else:
    tm3 = tm1 - tm
    print('{:.16f}'.format(min(ans, (H + N - 1 + D * tm3) // N * after)))
