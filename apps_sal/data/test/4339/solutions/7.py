def go():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dif = sorted(aa - bb for aa, bb in zip(a, b))
    j = n - 1
    res = 0
    for i, d in enumerate(dif):
        while j > -1 and d + dif[j] > 0:
            j -= 1
        res += n - 1 - j
        if j < i:
            res -= 1
    return res // 2


for _ in range(1):
    print(go())
