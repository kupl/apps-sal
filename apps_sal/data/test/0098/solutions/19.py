def solve(cnt, f1, f2, f3, nowx, nowy, cur):
    if nowx < 0 or nowy < 0 or cur < 0:
        return False
    if f1 == 1 and f2 == 1 and (f3 == 1):
        return True
    else:
        if f1 != 1:
            return solve(cnt + 1, 1, 0, 0, a, b, cur) or solve(cnt + 1, 1, 0, 0, b, a, cur)
        if f2 != 1:
            return solve(cnt + 1, 1, 1, 0, nowx - a1, nowy, nowy - b1) or solve(cnt + 1, 1, 1, 0, nowx - b1, nowy, nowy - a1)
        if f3 != 1:
            return solve(cnt + 1, 1, 1, 1, nowx - a2, nowy, nowy - b2) or solve(cnt + 1, 1, 1, 1, nowx - b2, nowy, nowy - a2)


(a, b) = map(int, input().split())
(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
if solve(0, 0, 0, 0, 0, 0, 0):
    print('YES')
else:
    print('NO')
