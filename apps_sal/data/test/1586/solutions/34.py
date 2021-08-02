n = int(input())

if n % 2 == 1:
    print('0')

else:
    five = 0
    two = 0
    for i in range(1, n):
        f = n // (2 * (5**i))
        t = n // (2**i)
        if f == t == 0:
            break
        five += f
        two += t
    print(min(five, two))
