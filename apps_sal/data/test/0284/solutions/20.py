n = int(input())
A = 1234567
B = 123456
C = 1234
ans = 'NO'
for a in range(n // A + 1):
    for b in range((n - A * a) // B + 1):
        if (n - a * A - b * B) % C == 0 and n - a * A - b * B >= 0:
            ans = 'YES'
print(ans)
