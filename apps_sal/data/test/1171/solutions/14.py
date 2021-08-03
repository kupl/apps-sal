n, k = list(map(int, input().split()))
v = list(map(int, input().split()))

ans = -10**9
for back in range(n + 1):
    for left in range(min(k - back + 1, n + 1)):
        for right in range(min(k - back - left + 1, n - left + 1)):
            hand = []
            hand.extend(v[:left])
            if right > 0:
                hand.extend(v[-right:])
            hand.sort()
            ans = max(ans, sum(hand[back:]))

print(ans)
