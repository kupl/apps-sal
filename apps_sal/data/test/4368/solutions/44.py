def main():
    t, n = list(map(int, input().split()))
    binary = 0
    ctr = 0
    temp = t
    while(temp > 0):
        binary = ((temp % n) * (10**ctr)) + binary
        temp = int(temp / n)
        ctr += 1
    return len(str(binary))


def __starting_point():
    print((main()))


__starting_point()
