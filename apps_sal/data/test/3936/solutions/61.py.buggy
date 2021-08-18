N = int(input())
dominoes = tuple(tuple(input()) for _ in range(2))
# print(*dominoes)
if N == 1:
    print(3)
    return

ans = 0
MOD = 10 ** 9 + 7
before_vertical = False
if dominoes[0][0] == dominoes[1][0]:
    ans += 3
    now = 1
    before_vertical = True
else:
    ans += 6
    now = 2

while now < N:
    if before_vertical:
        if dominoes[0][now] == dominoes[1][now]:
            ans *= 2
            now += 1
        else:
            ans *= 2
            now += 2
            before_vertical = False
    else:
        if dominoes[0][now] == dominoes[1][now]:
            ans *= 1
            now += 1
            before_vertical = True
        else:
            ans *= 3
            now += 2
    ans %= MOD
print(ans)
