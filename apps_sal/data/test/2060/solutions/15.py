def test():
    x = int(input())
    for b in range(20):
        t = x - 7 * b
        if t >= 0 and t % 3 == 0:
            print('YES')
            return
    print('NO')


n = int(input())

for _ in range(n):
    test()
