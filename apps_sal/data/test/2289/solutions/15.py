import bisect
(n, q) = list(map(int, input().split()))
warrior = list(map(int, input().split()))
attacker = list(map(int, input().split()))
warriors_new = []
sm = 0
for i in warrior:
    sm += i
    warriors_new.append(sm)
query = 0
ans = 0
for i in attacker:
    query += i
    if query >= warriors_new[n - 1]:
        query = 0
        ans = 0
    else:
        ans = bisect.bisect_right(warriors_new, query, ans)
    print(n - ans)
