t = int(input())
for _ in range(t):
    s, i, e = list(map(int, input().split()))
    if s + e <= i:
        print(0)
        continue
    if i + e < s:
        print(e + 1)
        continue
    mx = s + e
    dif = abs(s - i)
    if s > i:
        i += dif
    else:
        s += dif
    e -= dif
    mn = s + e // 2 + 1
    print(mx - mn + 1)
