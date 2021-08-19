def f(sa, sb):
    ans = 0
    for i in range(len(sa)):
        ans += sa[i] != sb[i]
    return ans


def third(a0, b0):
    if a0 != "a" and b0 != "a":
        return "a"
    if a0 != "b" and b0 != "b":
        return "b"
    if a0 != "c" and b0 != "c":
        return "c"


n, t = list(map(int, input().split()))
s1 = input()
s2 = input()
sovp = n - f(s1, s2)  # совпадающих из нашей строки
needsovp = n - t  # необходимо совпадающих
ans = [0] * n
need1r = needsovp - sovp
need2r = needsovp - sovp
if sovp >= needsovp:
    for i in range(n):
        if s1[i] != s2[i]:
            ans[i] = third(s1[i], s2[i])
        elif needsovp > 0:
            ans[i] = s1[i]
            needsovp -= 1
        else:
            ans[i] = third(s1[i], s2[i])
    if not(f("".join(ans), s1) == f("".join(ans), s2) == t):
        print(-1)
    else:
        print(*ans, sep="")
else:
    for i in range(n):
        if s1[i] != s2[i]:
            if need1r > 0:
                need1r -= 1
                ans[i] = s1[i]
            elif need2r > 0:
                need2r -= 1
                ans[i] = s2[i]
            else:
                ans[i] = third(s1[i], s2[i])
        else:
            ans[i] = s1[i]
    if not(f("".join(ans), s1) == f("".join(ans), s2) == t):
        print(-1)
    else:
        print(*ans, sep="")
