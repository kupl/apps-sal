t = int(input())
for q in range(0, t):
    n = int(input())
    number = 0
    while n > 1:
        left = 1
        right = n
        while right - left > 1:
            m = (right + left) // 2
            if 3 * m * (m + 1) // 2 - m > n:
                right = m
            else:
                left = m
        n -= (3 * left * (left + 1) // 2 - left)
        number += 1
    print(number)

