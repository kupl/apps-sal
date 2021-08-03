from math import ceil
n, m = list(map(int, input().split()))
if n % 2 == 0:
    a = n // 2
    b = a
else:
    b = n // 2
    a = b + 1
l = 0
l = (n**2)
if l % 2 == 0:
    l = l // 2
    l += 0
else:
    l = l // 2
    l += 1
ans = ""
for i in range(m):
    q1, q2 = list(map(int, input().split()))
    if (q1 + q2) % 2 == 0:
        x = (q1 - 1) // 2
        y = ceil((q1 - 1) / 2)
        na = (y * a) + x * b
        if q1 % 2 != 0:
            w = ceil(q2 / 2)
        else:
            w = q2 // 2
        ans += str(na + w) + chr(10)
    else:
        x = (q1 - 1) // 2
        y = ceil((q1 - 1) / 2)
        na = (y * b) + x * a
        if q1 % 2 == 0:
            w = ceil(q2 / 2)
        else:
            w = q2 // 2
        ans += str(na + w + l) + chr(10)

print(ans)
