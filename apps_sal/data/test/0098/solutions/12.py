(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
(a3, b3) = map(int, input().split())
if max(a2, a3) <= a1 and b2 + b3 <= b1 or (max(a2, b3) <= a1 and b2 + a3 <= b1) or (max(b2, a3) <= a1 and a2 + b3 <= b1) or (max(b2, b3) <= a1 and a2 + a3 <= b1) or (a2 + a3 <= a1 and max(b2, b3) <= b1) or (a2 + b3 <= a1 and max(b2, a3) <= b1) or (b2 + a3 <= a1 and max(a2, b3) <= b1) or (b2 + b3 <= a1 and max(a2, a3) <= b1):
    print('YES')
else:
    print('NO')
