import sys
T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    ans = 0
    c = 1
    L = []
    for i in range(1, n):
        if s[i] == s[i - 1]:
            c = c + 1
        else:
            L.append(c)
            c = 1
    if len(L) == 0:
        if c <= 2:
            print(0)
        else:
            print((c + 2) // 3)
    else:
        if len(L) % 2 == 0:
            L[0] = L[0] + c
        else:
            L.append(c)
        for l in L:
            ans = ans + l // 3
        print(ans)
