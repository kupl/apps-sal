t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split(' ')))
    M = []
    for i in range(n):
        M.append(list(map(int, input().split(' '))))
    lo = 0
    hi = n + m - 2
    total = 0
    while True:
        if lo >= hi:
            break
        num1 = 0
        num0 = 0
        for i in range(lo + 1):
            j = lo - i
            if i < n and j < m and (j >= 0):
                if M[i][j] == 1:
                    num1 += 1
                else:
                    num0 += 1
        for i in range(hi + 1):
            j = hi - i
            if i < n and j < m and (j >= 0):
                if M[i][j] == 1:
                    num1 += 1
                else:
                    num0 += 1
        total += min(num0, num1)
        lo += 1
        hi -= 1
    print(total)
