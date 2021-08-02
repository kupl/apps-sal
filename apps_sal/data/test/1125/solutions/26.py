N = int(input())
A = list(map(int, input().split()))

xor = 0
for a in A[2:]:
    xor ^= a

n = A[0] + A[1] - xor
if n < 0 or n % 2:
    print(-1)
    return

n //= 2
a = b = 0
digit = 1
d = []
while n or xor:
    n0 = n & 1; xor0 = xor & 1
    if n0:
        if xor0:
            print(-1)
            return
        else:
            a += digit
            b += digit
    else:
        if xor0:
            b += digit
            d.append(digit)

    digit *= 2
    n >>= 1; xor >>= 1

if a > A[0]:
    print(-1)
    return

while d:
    dd = d.pop()
    if a + dd <= A[0]:
        a += dd; b -= dd

if a:
    print(A[0] - a)
else:
    print(-1)
