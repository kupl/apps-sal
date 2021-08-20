(a, b) = list(map(int, input().split()))


def gcd(arg1, arg2):
    if arg1 == 0:
        return arg2
    if arg2 == 0:
        return arg1
    if arg2 > arg1:
        (arg2, arg1) = (arg1, arg2)
    return gcd(arg1 % arg2, arg2)


if a > b:
    (a, b) = (b, a)
k = b - a
array = []
i = 1
while i ** 2 <= k:
    if k % i == 0:
        array.append(i)
        array.append(k // i)
    i += 1
gcdis = a * b / gcd(a, b)
z = 0
for d in array:
    z1 = a - a % d + d
    z2 = b - b % d + d
    if z1 * z2 // gcd(z1, z2) <= gcdis:
        if z1 * z2 // gcd(z1, z2) == gcdis:
            z = min(d - a % d, z)
        else:
            gcdis = z1 * z2 // gcd(z1, z2)
            z = d - a % d
print(z)
