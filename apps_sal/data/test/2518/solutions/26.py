n, a, b = list(map(int, input().split()))
h = [int(input()) for i in range(n)]
maxim_h = max(h)

ok = (maxim_h + a - 1) // a * n
ng = 0
while abs(ok - ng) > 1:

    X = (ok + ng) // 2

    cnt = 0
    flag = 1
    for val in h:
        if val <= b * X:
            continue
        temp = (val - b * X + a - b - 1) // (a - b)
        cnt += temp

        if cnt > X:
            flag = 0
            break

    if flag:
        ok = X
    else:
        ng = X
print(ok)
