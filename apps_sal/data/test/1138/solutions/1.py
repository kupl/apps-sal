s = str(input())
n = len(s)
r = 0
if n % 2:
    print(-1)
else:
    U = D = L = R = 0
    for i in range(n):
        if s[i] == "L":
            L += 1
        elif s[i] == "R":
            R += 1
        elif s[i] == "U":
            U += 1
        else:
            D += 1
    if (U + D) % 2:
        r = 1
        if U > D:
            D += 1
            if R > L:
                R -= 1
            else:
                L -= 1
        else:
            U += 1
            if R > L:
                R -= 1
            else:
                L -= 1
    print(r + abs(U - D) // 2 + abs(R - L) // 2)
