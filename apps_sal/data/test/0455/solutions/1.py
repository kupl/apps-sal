def main():
    N = int(input())
    xy = []
    for _ in range(N):
        (x, y) = list(map(int, input().split()))
        xy.append((x, y))
    mod = sum(xy[0]) % 2
    for (x, y) in xy:
        if (x + y) % 2 != mod:
            print(-1)
            return
    print(33 - mod)
    D = [2 ** i for i in range(31, -1, -1)]
    if mod == 0:
        D.append(1)
    print(' '.join(map(str, D)))
    for (x, y) in xy:
        temp = []
        for d in D:
            if x >= y and x + y >= 0:
                temp.append('R')
                x -= d
            elif x < y and x + y >= 0:
                temp.append('U')
                y -= d
            elif x >= y and x + y < 0:
                temp.append('D')
                y += d
            else:
                temp.append('L')
                x += d
        print(''.join(temp))


main()
