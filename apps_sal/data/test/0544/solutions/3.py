T = int(input())

for t in range(T):
    n = int(input())
    s = list(input())

    ok = True
    for i in range(n // 2):
        d = abs(ord(s[i]) - ord(s[-i - 1]))
        if d > 2 or d == 1:
            ok = False

    print(["NO", "YES"][ok])
