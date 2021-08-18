K = int(input())
a = K
while a % 2 == 0:
    a //= 2
while a % 5 == 0:
    a //= 5
if a == 1:
    print(1)
else:
    mod = set([])
    a = 1
    while a not in mod:
        mod.add(a)
        a *= 10
        a %= K

    mod = list(mod)
    n = len(mod)
    wei = pow(2, K) - 1
    check = 1
    ans = 0
    for j in range(0, n):
        ans = ans | (check << mod[j])
    check = ans
    for i in range(1, 46):
        if check >> 0 & 1 == 1:
            print(i)
            return
        ans = check
        for j in range(0, n):
            ans = ans | (check << mod[j])
        ans1 = ans & wei
        ans2 = ans >> K
        check = ans1 | ans2
