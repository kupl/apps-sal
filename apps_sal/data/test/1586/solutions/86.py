N = int(input())

if N % 2 == 0:
    Ans = 0
    p = 1
    check = 0
    while check != 0 or p == 1:
        check = N // (2 * 5**p)
        Ans += check
        p += 1
    print(Ans)

else:
    print(0)
