s = input()
ans1 = s[0]


def solve(i, tmp, ans):
    nonlocal ans1
    if i == 3:
        if tmp == 7:
            ans1 = ans
            return True
        else:
            return False

    if solve(i + 1, tmp + int(s[i + 1]), ans + "+" + s[i + 1]): return True
    if solve(i + 1, tmp - int(s[i + 1]), ans + "-" + s[i + 1]): return True


if solve(0, int(s[0]), ans1):
    print(ans1 + "=7")
