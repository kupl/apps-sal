(N, P) = map(int, input().split())
S = input()
if P == 2:
    ans = 0
    for (i, d) in enumerate(map(int, S)):
        if d % 2 == 0:
            ans += i + 1
    print(ans)
elif P == 5:
    ans = 0
    for (i, d) in enumerate(map(int, S)):
        if d % 5 == 0:
            ans += i + 1
    print(ans)
else:
    mods = [0] * P
    mods[0] = 1
    cur_mod = 0
    for (i, digit) in enumerate(map(int, S)):
        cur_mod += pow(10, N - i - 1, P) * digit
        cur_mod %= P
        mods[cur_mod] += 1
    ans = 0
    for count in mods:
        ans += count * (count - 1) // 2
    print(ans)
