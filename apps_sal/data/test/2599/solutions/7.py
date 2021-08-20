for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ans = float('inf')
    for m in range(20):
        for l in range(10):
            if k + l <= 9:
                dsum = n - k * (k + 1) // 2
                if dsum % (k + 1) == 0:
                    f = dsum // (k + 1)
                    f -= l
                    if f >= 0:
                        if 9 > f:
                            test = str(f) * (f != 0) + str(l)
                            ans = min(ans, int(test))
                        else:
                            q = f // 9
                            r = f % 9
                            test = str(r) * (r != 0) + '9' * q + str(l)
                            test = int(test)
                            ans = min(test, ans)
            else:
                dsum = n - (k + l - 9) * (1 - 9 * m - l) - (9 - l) * (10 - l) // 2 - (k + l - 9) * (k + l - 10) // 2
                if dsum % (k + 1) == 0:
                    f = dsum // (k + 1)
                    f -= 9 * m + l
                    if f >= 0:
                        if 9 > f:
                            test = str(f) * (f != 0) + '9' * m + str(l)
                            ans = min(ans, int(test))
                        else:
                            f -= 8
                            q = f // 9
                            r = f % 9
                            test = str(r) * (r != 0) + '9' * q + '8' + '9' * m + str(l)
                            test = int(test)
                            ans = min(test, ans)
    if ans != float('inf'):
        print(ans)
    else:
        print(-1)
