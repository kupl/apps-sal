a, b, f, k = list(map(int, input().split()))
i = 0
bi = b
ans = 0
while i < k:
    if f > bi:
        print(-1)
        return
    bi -= f
    if k - i == 1:
        if a - f > bi:
            bi = b
            ans += 1
        if a - f > b:
            print(-1)
            return
        break
    i += 1
    if 2 * (a - f) > bi:
        bi = b
        ans += 1
    if 2 * (a - f) > b:
        print(-1)
        return
    bi -= 2 * (a - f)
    if k - i == 1:
        if f > bi:
            bi = b
            ans += 1
        break
    if 2 * f > bi:
        bi = b
        ans += 1
    if 2 * f > b:
        print(-1)
        return
    bi -= f
    i += 1
print(ans)
