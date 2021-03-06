from heapq import heappush, heappop
n = int(input())
L = list(map(int, input().split()))
T = input()
ans = sum(L)
Q = []
for (l, t) in zip(L, T):
    if t == 'G':
        heappush(Q, (2, 2 * l))
        heappush(Q, (5, float('inf')))
    elif t == 'W':
        heappush(Q, (1, 2 * l))
        heappush(Q, (3, float('inf')))
    need_stamina = l
    while need_stamina > 0:
        (cost, quantity) = heappop(Q)
        if need_stamina > quantity:
            ans += quantity * cost
            need_stamina -= quantity
        else:
            ans += need_stamina * cost
            heappush(Q, (cost, quantity - need_stamina))
            need_stamina = 0
print(ans)
