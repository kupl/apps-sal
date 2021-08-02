def solve(x):
    brr = []
    while x > 0:
        brr.append(x % 2)
        x //= 2

    def check(brr):
        return all(brr)

    cnt = 0
    ops = []

    while not check(brr):
        if cnt % 2 == 0:
            n = None
            for i in range(len(brr) - 1, -1, -1):
                if brr[i] == 0:
                    n = i
                    break
            ops.append(n + 1)
            for i in range(n, -1, -1):
                brr[i] = 1 - brr[i]
        else:
            for i in range(len(brr)):
                if brr[i] == 0:
                    brr[i] = 1
                    break
                else:
                    brr[i] = 0
        cnt += 1

    print(cnt)
    print(' '.join(map(str, ops)))


solve(int(input()))
