a, b, c = list(map(int, input().split()))
s = []
while a != 0:
    t = 0
    while a < b:
        if t == 1:
            s.append([0, 0])
            if c == 0:
                print(len(s))
                return
        a *= 10
        t = 1
    d = a // b
    a %= b
    if [d, a] in s:
        print(-1)
        return
    elif d == c:
        print(len(s) + 1)
        return
    s.append([d, a])
    if a == 0 and c == 0:
        print(len(s) + 1)
        return
print(-1)
