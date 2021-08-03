from fractions import gcd


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm(numbers):
    x = numbers[0]
    for y in numbers:
        x = lcm_base(x, y)
    return x


N, M = list(map(int, input().split()))
aaa = list(map(int, input().split()))
a = aaa[0]
cnt = 0
while a % 2 == 0:
    cnt += 1
    a //= 2
for a in aaa:
    if a % 2 ** cnt != 0 or a % 2 ** (cnt + 1) == 0:
        print((0))
        return
bbb = [a // 2 for a in aaa]
lc = lcm(bbb)
q, r = divmod(M // lc, 2)
print((q + r))
