s, x = list(map(int, input().split()))
f = 0
if s == x:
    f = -2
aa = s - x
if aa % 2 == 1 or aa < 0:
    print(0)
else:
    a = aa // 2
    # print(a,s)
    out = 1
    for i in range(64):
        xx = x % 2
        aa = a % 2
        if xx == 1:
            out *= 2
            if aa == 1:
                out = 0
        x //= 2
        a //= 2
    print(out + f)
