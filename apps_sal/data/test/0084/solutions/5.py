n = int(input())
max9 = 1
while (int('9' * max9) + 1) // 2 <= n:
    max9 += 1
max9 -= 1
k = 0
ans = 0
f = True
while f:
    number = int(str(k) + '9' * max9)
    b = min(number - 1, n)
    a = number // 2 + 1
    if a <= b:
        m = b - a + 1
        ans += m
        k += 1
    else:
        f = False
if n == 2:
    print(1)
elif n == 3:
    print(3)
elif n == 4:
    print(6)
else:
    print(ans)
