
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    S = stdin.readline()
    S = S[:-1]

    rnum = 0
    lnum = 0

    if "L" not in S or "R" not in S:
        print((n + 2) // 3)
        continue

    for i in range(n - 1):
        if S[i] != S[i + 1]:
            S = S[i + 1:] + S[:i + 1]
            break

    ans = 0
    for i in S:
        if i == "R":
            rnum += 1
            ans += (lnum) // 3
            lnum = 0
        else:
            lnum += 1
            ans += (rnum) // 3
            rnum = 0

    if lnum >= 3:
        ans += (lnum) // 3
    if rnum >= 3:
        ans += (rnum) // 3

    print(ans)
