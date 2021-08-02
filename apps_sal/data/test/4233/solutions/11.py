def main():
    inp = []
    n, m = list(map(int, input().split()))
    remaining = 0
    for _ in range(n):
        cur_inp = input()
        inp.append(cur_inp)
        remaining += cur_inp.count("*")
    remaining2 = [[True] * m for _ in range(n)]
    res = []
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if inp[x][y] == "*":
                last_size = None
                for size in range(1, min(x + 1, n - x, y + 1, m - y)):
                    if inp[x - size][y] == inp[x + size][y] == inp[x][y - size] == inp[x][y + size] == "*":
                        for x1, y1 in (x - size, y), (x + size, y), (x, y - size), (x, y + size):
                            if remaining2[x1][y1]:
                                remaining -= 1
                                remaining2[x1][y1] = False
                        last_size = size
                    else:
                        break
                if last_size is not None:
                    if remaining2[x][y]:
                        remaining -= 1
                        remaining2[x][y] = False
                    res.append((x + 1, y + 1, last_size))
    if remaining:
        print('-1')
    else:
        print(len(res))
        for x in res:
            print(*x)


main()
