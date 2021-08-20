def Check(a2, b2, a3, b3):
    if a1 >= a2 + a3 and b1 >= max(b2, b3) or (a1 >= max(a2, a3) and b1 >= b2 + b3):
        return True
    else:
        return False


(a1, b1) = list(map(int, input().split()))
(a2, b2) = list(map(int, input().split()))
(a3, b3) = list(map(int, input().split()))
(a1, b1) = (min(a1, b1), max(a1, b1))
(a2, b2) = (min(a2, b2), max(a2, b2))
(a3, b3) = (min(a3, b3), max(a3, b3))
r = Check(a2, b2, a3, b3) or Check(a2, b2, b3, a3) or Check(b2, a2, a3, b3) or Check(b2, a2, b3, a3)
if r:
    print('YES')
else:
    print('NO')
