t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    mod_0, mod_1, mod_2 = 0, 0, 0
    for el in arr:
        if el % 3 == 0:
            mod_0 += 1
        elif el % 3 == 1:
            mod_1 += 1
        elif el % 3 == 2:
            mod_2 += 1

    res = mod_0

    min_1_2 = min(mod_1, mod_2)
    res += min_1_2
    mod_1 -= min_1_2
    mod_2 -= min_1_2

    res += mod_1 // 3
    res += mod_2 // 3
    print(res)
