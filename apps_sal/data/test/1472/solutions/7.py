(N, X, Y) = map(int, input().split())
p = Y - X + 1
arm_a = X - 1
arm_b = N - Y
if p % 2:
    for i in range(1, N):
        ans = 0
        if i * 2 < p:
            ans += p
        if 1 < i <= p // 2 + arm_a:
            ans += 2 * min(arm_a, p // 2, arm_a + p // 2 - i + 1, i - 1)
        if 1 < i <= p // 2 + arm_b:
            ans += 2 * min(arm_b, p // 2, arm_b + p // 2 - i + 1, i - 1)
        if i <= arm_a:
            ans += arm_a - i + 1
        if i <= arm_b:
            ans += arm_b - i + 1
        if 2 < i <= arm_a + arm_b + 1:
            ans += min(arm_a, arm_b, arm_a + arm_b - i + 2, i - 2)
        print(ans)
else:
    for i in range(1, N):
        ans = 0
        if i * 2 < p:
            ans += p
        elif i * 2 == p:
            ans += p // 2
        if 1 < i < p // 2 + arm_a:
            ans += 2 * min(arm_a, p // 2 - 1, arm_a + p // 2 - i, i - 1)
        if p // 2 < i <= p // 2 + arm_a:
            ans += 1
        if 1 < i < p // 2 + arm_b:
            ans += 2 * min(arm_b, p // 2 - 1, arm_b + p // 2 - i, i - 1)
        if p // 2 < i <= p // 2 + arm_b:
            ans += 1
        if i <= arm_a:
            ans += arm_a - i + 1
        if i <= arm_b:
            ans += arm_b - i + 1
        if 2 < i <= arm_a + arm_b + 1:
            ans += min(arm_a, arm_b, arm_a + arm_b - i + 2, i - 2)
        print(ans)
