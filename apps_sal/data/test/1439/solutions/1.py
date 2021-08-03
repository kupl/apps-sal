(n, m) = map(int, input().split())
if n > 2 * m:
    print("YES")
else:
    t = [0 for i in range(m)]
    s = input().split()
    for i in range(len(s)):
        h = int(s[i]) % m
        v = [0 for i in range(m)]
        for j in range(m):
            if t[j] == 1:
                v[(h + j) % m] = 1
        for j in range(m):
            if v[j] == 1:
                t[j] = 1
        t[h] = 1
    if t[0] == 1:
        print("YES")
    else:
        print("NO")
