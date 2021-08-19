import copy
N = int(input())


def power_func(a, n, p):  # a**n mod p
    bi = str(format(n, "b"))  # 2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


mod = 10 ** 9 + 7
c = [0] * 4
for i in range(4):
    c[i] = str(input())

if c[0] == "A" and c[1] == "A":
    ans = 1
elif c[1] == "B" and c[3] == "B":
    ans = 1
elif c in [["B", "A", "A", "A"], ["B", "A", "A", "B"], ["A", "B", "B", "A"], ["B", "B", "B", "A"]]:
    if N == 2 or N == 3:
        ans = 1
    else:
        N -= 3
        one = 1
        two = 1
        while N != 0:
            x = one
            one += two
            one %= mod
            two = x
            N -= 1
            #print(one, two)
        ans = one
else:
    if N == 2 or N == 3:
        ans = 1
    else:
        ans = power_func(2, N - 3, mod)


print(ans)
