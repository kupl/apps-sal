s, m, cost = list(map(int, input().split()))

cnt = s // cost + m // cost
ost_s = s % cost
ost_m = m % cost

if ost_s + ost_m >= cost:
    print(cnt + 1, min(cost - ost_s, cost - ost_m))
else:
    print(cnt, 0)
