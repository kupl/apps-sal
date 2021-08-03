def kai():
    n = int(input())
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c > 0:
                ans += 1

            else:
                break
    return ans


print(kai())
