def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def abc169d_div_game():
    n = int(input())
    arr = factorization(n)
    cnt = 0
    for p, e in arr:
        if p == 1: continue
        for i in range(1, e+1):
            if e >= i:
                cnt += 1
                e -= i
            else:
                break
    print(cnt)

abc169d_div_game()
