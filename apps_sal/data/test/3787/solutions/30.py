from bisect import bisect_left
n, a, b = list(map(int, input().split()))

if n < a + b - 1 or a * b < n:
    print((-1))
    return

ans = []
now = a
for i in range(a, 0, -1):
    ans.append(i)

iran = a * b - n
now = a
for i in range(1, b):
    # このぐるーぷでは何個削るか
    not_need = min(iran, a - 1)
    iran -= not_need
    need = a - not_need

    prev = now
    now += need
    for j in range(now, prev, -1):
        ans.append(j)
print((*reversed(ans)))
