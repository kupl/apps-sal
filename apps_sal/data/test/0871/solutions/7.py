
def readline(): return tuple(map(int, input().split()))


def readlines(count):
    while count:
        count -= 1
        yield readline()


def main():
    n, s = readline()
    shedule = [h * 60 + m for (h, m) in readlines(n)]

    shedule.append(float('inf'))
    prev = -s

    for time in shedule:
        if prev + s < time - s:
            print(*divmod(prev + s, 60))
            break
        prev = time + 1


main()
