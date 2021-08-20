N = int(input())
X = 0
mod = int(1000000000.0) + 7
for i in range(4):
    X <<= 1
    X += ord(input()) - 65
F1 = {0, 1, 2, 3, 5, 7, 13, 15}
FF = {6, 8, 9, 14}
FB = {4, 10, 11, 12}
if X in F1:
    print(1)
elif X in FF:
    (a, b) = (1, 1)
    for i in range(N - 2):
        (a, b) = (b, a + b)
        b %= mod
    print(a % mod)
elif X in FB:
    t = N - 3
    b = 1
    while t > 0:
        b *= 2
        b %= mod
        t -= 1
    print(b)
