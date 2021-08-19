(n, a, b) = map(int, input().split())
s = input()
(k1, k2) = (0, 0)
for i in range(n + 1):
    for j in range(n + 1):
        if i * a + j * b == n:
            k1 = i
            k2 = j
            break
    if k1 or k2:
        break
else:
    print('-1')
if k1 or k2:
    print(k1 + k2)
    i = 0
    while k1:
        print(s[i:i + a])
        k1 -= 1
        i += a
    while k2:
        print(s[i:i + b])
        k2 -= 1
        i += b
