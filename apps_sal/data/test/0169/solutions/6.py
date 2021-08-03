n = int(input())
a = int(input())
b = int(input())
c = int(input())

d = b - c

if a <= d:
    print(n // a)

else:
    lb = 0
    ub = n

    while ub - lb > 1:
        mid = (ub + lb) // 2
        tmp = n - d * (mid - 1)
        if tmp >= b:
            lb = mid
        else:
            ub = mid

    ans = lb
    n -= d * lb
    ans += n // a
    print(ans)
