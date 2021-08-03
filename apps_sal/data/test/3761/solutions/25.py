S = input()
S += "E"
x, y = map(int, input().split())
go = [[], []]
idx = 0
while S[idx] == "F":
    x -= 1
    idx += 1
g = 1
idx += 1
while idx < len(S):
    now = 0
    while S[idx] == "F":
        now += 1
        idx += 1
    if now > 0:
        go[g].append(now)
    g = (g + 1) % 2
    idx += 1


def check(L, m):
    dp = {0}
    for x in L:
        dpc = dp.copy()
        dp = set()
        for now in dpc:
            dp |= {now + x, now - x}
    if m in dp:
        return True
    return False


if check(go[0], x) and check(go[1], y):
    print("Yes")
else:
    print("No")
