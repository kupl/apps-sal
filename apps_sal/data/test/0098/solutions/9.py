a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))
ans = ''
if (a1 > b1):
    a1, b1 = b1, a1
if (a2 > b2):
    a2, b2 = b2, a2
if (a3 > b3):
    a3, b3 = b3, a3
ans = 0
if (a2 + a3 <= a1) and (max(b2, b3) <= b1):
    ans += 1
if (a2 + b3 <= a1) and (max(b2, a3) <= b1):
    ans += 1
if (a3 + b2 <= a1) and (max(a2, b3) <= b1):
    ans += 1
if (b2 + b3 <= a1) and (max(a2, a3) <= b1):
    ans += 1
if (a2 + a3 <= b1) and (max(b2, b3) <= a1):
    ans += 1
if (a2 + b3 <= b1) and (max(b2, a3) <= a1):
    ans += 1
if (a3 + b2 <= b1) and (max(a2, b3) <= a1):
    ans += 1
if (b2 + b3 <= b1) and (max(a2, a3) <= a1):
    ans += 1
if (ans == 0):
    print('NO')
else:
    print('YES')
