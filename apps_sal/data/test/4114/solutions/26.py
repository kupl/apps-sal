n = int(input())
if n == 1:
    x, y, h = map(int, input().split())
    print(x, y, h)
    return
s = [list(map(int, input().split())) for _ in range(n)]
for i in range(101):
    for j in range(101):
        h = -1
        ok = 1
        for t in s:
            if t[2] == 0:
                ok += 1
            elif h == -1:
                h = abs(t[0] - i) + abs(t[1] - j) + t[2]
            else:
                h0 = abs(t[0] - i) + abs(t[1] - j) + t[2]
                if h == h0:
                    ok += 1
        if ok == n:
            for t in s:
                if abs(t[0] - i) + abs(t[1] - j) <= h:
                    if not h == abs(t[0] - i) + abs(t[1] - j) + t[2]:
                        ok = 0
                else:
                    if not t[2] == 0:
                        ok = 0
            if ok == n:
                print(i, j, h)
                return
