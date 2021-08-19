n = int(input())
s1 = input()
s2 = input()
if s1[0] == s2[0]:
    a = 3
    l = 0
    v = True
else:
    a = 6
    l = 1
    v = False
mod = 10 ** 9 + 7


def mult_mod(x, y):
    return x * y % mod


while l + 1 < n:
    if v:
        if s1[l + 1] == s2[l + 1]:
            l += 1
            a = mult_mod(a, 2)
        else:
            l += 2
            a = mult_mod(a, 2)
            v = False
    elif s1[l + 1] == s2[l + 1]:
        l += 1
        v = True
    else:
        l += 2
        a = mult_mod(a, 3)
print(a % mod)
