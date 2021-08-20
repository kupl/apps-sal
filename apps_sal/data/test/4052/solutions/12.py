t = 1
for test in range(1, t + 1):
    n = int(input())
    s = list(input())
    t = list(input())
    s1 = list(s)
    t1 = list(t)
    s1.sort()
    t1.sort()
    if s1 != t1:
        print(-1)
        continue
    count = 0
    moves = []
    for i in range(n):
        tmp = i + s[i:].index(t[i])
        count += tmp - i
        for j in range(tmp - 1, i - 1, -1):
            (s[j], s[j + 1]) = (s[j + 1], s[j])
            moves.append(j + 1)
    print(count)
    print(*moves)
