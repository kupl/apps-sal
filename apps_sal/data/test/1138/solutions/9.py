s = input()
ans = 0

if len(s) % 2 != 0:
    print(-1)
else:
    u = s.count('U')
    d = s.count('D')
    r = s.count('R')
    l = s.count('L')
    if abs(u - d) % 2 == 0 and abs(r - l) % 2 == 0:
        ans = abs(u - d) // 2 + abs(r - l) // 2
    else:
        ans = abs(u - d) // 2 + abs(r - l) // 2 + 1
    print(ans)
