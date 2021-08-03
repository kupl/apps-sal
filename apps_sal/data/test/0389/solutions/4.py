a, b = map(int, input().split())
k = a
l = b
a2, a3, a5 = 0, 0, 0
b2, b3, b5 = 0, 0, 0
while k:
    if k % 2 == 0:
        a2 += 1
        k = k / 2
    elif k % 3 == 0:
        a3 += 1
        k = k / 3
    elif k % 5 == 0:
        a5 += 1
        k = k / 5
    else:
        break

while l:
    if l % 2 == 0:
        b2 += 1
        l = l / 2
    elif l % 3 == 0:
        b3 += 1
        l = l / 3
    elif l % 5 == 0:
        b5 += 1
        l = l / 5
    else:
        break
if k != l:
    print(-1)
else:
    print(max(a2, b2) - min(a2, b2) + max(a3, b3) - min(a3, b3) + max(a5, b5) - min(a5, b5))
