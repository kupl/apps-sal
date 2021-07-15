n, k = map(int, input().split())

xs = [i for i in range(1, k + 1)]
xs.reverse()

dict_x = {}

mod = 10 ** 9 + 7

def pow(x, y):
    nonlocal mod
    a = 1
    b = x
    c = y
    while c > 0:
        if c & 1:
            a = (a * b) % mod
        b = (b * b) % mod
        c = c >> 1
    return a

answer = 0
for x in xs:
    num = k // x
    a = pow(num, n)
    # print(a)
    s = 2
    while x * s <= k:
        a -= dict_x[x * s]
        s += 1
    dict_x[x] = a
    answer = (answer + a * x) % mod

print(answer)
