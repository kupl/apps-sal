mod = 10**9 + 7

n = int(input())

s = input()

em = 1
a = 0
ab = 0
abc = 0

for cur_c in s:
    new_em = 0
    new_a = 0
    new_ab = 0
    new_abc = 0

    opts = [cur_c]
    if cur_c == "?":
        opts = ['a', 'b', 'c']

    for c in opts:
        new_em += em
        new_a += a
        new_ab += ab
        new_abc += abc
        if c == 'a':
            new_a += em
        elif c == 'b':
            new_ab += a
        else:
            new_abc += ab
    em = new_em % mod
    a = new_a % mod
    ab = new_ab % mod
    abc = new_abc % mod

print(abc)
