def Yeee (x, v, n) :
    re = 0
    pre = 0
    sum = 1
    cnt = [0] * n + [1] + [0] * n
    for i in v :
        if(i < x) :
            pre += 1
            sum += cnt[pre + n]
        else :
            sum -= cnt[pre + n]
            pre -= 1
        cnt[pre + n] += 1
        re += sum
    return re
n, x = list(map(int, input().split()))
v = [int(i) for i in input().split()]
print(Yeee(x + 1, v, n) - Yeee(x, v, n))

