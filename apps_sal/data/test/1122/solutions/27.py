n, m = map(int, input().split())
if m % 2 == 1:

    cnt = 0

    for i in range(m // 2):
        num1 = 1 + i
        num2 = m - i
        print(num1, num2, sep=" ")
        cnt += 1
        if cnt == m:
            return
    for i in range(m // 2 + 1):
        num1 = m + 1 + i
        num2 = 2 * m + 1 - i
        print(num1, num2, sep=" ")
        cnt += 1
        if cnt == m:
            return
else:
    cnt = 0

    for i in range(m // 2):
        num1 = 1 + i
        num2 = m + 1 - i
        print(num1, num2, sep=" ")
        cnt += 1
        if cnt == m:
            return
    for i in range(m // 2):
        num1 = m + 2 + i
        num2 = 2 * m + 1 - i
        print(num1, num2, sep=" ")
        cnt += 1
        if cnt == m:
            return

