for _ in range(int(input())):
    n = int(input())
    x = n
    twos = 0
    threes = 0
    while x % 2 == 0:
        x //= 2
        twos += 1
    while x % 3 == 0:
        x //= 3
        threes += 1
    if x == 1 and threes >= twos:
        print(threes + threes - twos)
    else:
        print(-1)

