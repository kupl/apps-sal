s = input()
n = len(s)
ans = 0
if n % 2 == 1:
    print("-1")
else:
    p = 0
    q = 0
    for i in range(0, n):
        if s[i] == "R":
            p += 1
        elif s[i] == "U":
            q += 1
        elif s[i] == "L":
            p -= 1
        elif s[i] == "D":
            q -= 1
    if p % 2 == 0:
        ans = abs(p // 2) + abs(q // 2)
    else:
        ans1 = min(abs(p - 1), abs(p + 1))
        ans2 = min(abs(q - 1), abs(q + 1))
        ans = (ans1 + ans2) // 2 + 1
    print(ans)
