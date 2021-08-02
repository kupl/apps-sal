s = int(input())


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


coll = s
i = 1
while 1:
    if coll == 1 or coll == 2 or coll == 4:
        print(i + 3)
        break
    coll = collatz(coll)
    i += 1
