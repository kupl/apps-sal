n = input()
k = int(input())
l = len(n)


def k2(l, n):
    ans = 81 * (l - 1) * (l - 2) // 2
    ans += (int(n[0]) - 1) * 9 * (l - 1)
    for i, s in enumerate(n[1:]):
        if s == "0":
            continue
        ans += int(s)
        ans += max((l - i - 2), 0) * 9
        break
    return ans


if k == 1:
    ans = (l - 1) * 9 + int(n[0])
elif k == 2:
    if l == 1:
        print(0)
        return
    ans = k2(l, n)
else:
    if l < 3:
        print(0)
        return
    ans = 9 ** 3 * (l - 1) * (l - 2) * (l - 3) // 6
    ans += (int(n[0]) - 1) * 81 * (l - 1) * (l - 2) // 2
    n = n[1:]
    n = str(int(n))
    ans += k2(len(n), n)
print(ans)
