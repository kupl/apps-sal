import time


def test(size_x, size_y, x1, y1, x2, y2):
    if x1 + x2 <= size_x and y1 <= size_y and (y2 <= size_y):
        return 1
    return 0


(A, B) = (int(i) for i in input().split())
(a1, b1) = (int(i) for i in input().split())
(a2, b2) = (int(i) for i in input().split())
start = time.time()
ans = 0
ans += test(A, B, a1, b1, a2, b2)
ans += test(A, B, a1, b1, b2, a2)
ans += test(A, B, b1, a1, a2, b2)
ans += test(A, B, b1, a1, b2, a2)
ans += test(B, A, a1, b1, a2, b2)
ans += test(B, A, a1, b1, b2, a2)
ans += test(B, A, b1, a1, a2, b2)
ans += test(B, A, b1, a1, b2, a2)
if ans > 0:
    print('YES')
else:
    print('NO')
finish = time.time()
