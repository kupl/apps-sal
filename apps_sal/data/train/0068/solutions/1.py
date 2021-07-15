import sys

T = int(sys.stdin.readline().strip())
for t in range (0, T):
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    L = [1]
    for i in range (1, n):
        if s[i] == s[i-1]:
            L[-1] = L[-1] + 1
        else:
            L.append(1)
    L.reverse()
    i = n - 1
    ans = 0
    while len(L) > 0:
        ans = ans + 1
        v = True
        i = min(i, len(L) - 1)
        while i >= 0 and v == True:
            if L[i] == 1:
                i = i - 1
                if i == -1:
                    v = False
            else:
                v = False
        if i == -1:
            L.pop()
        else:
            L[i] = L[i] - 1
        if len(L) > 0:
            L.pop()
    print(ans)

