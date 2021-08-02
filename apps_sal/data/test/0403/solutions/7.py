def main():
    read = lambda: list(map(int, input().split()))
    n, x, y = read()
    a = sorted(read())
    cnt = 0
    for k in a:
        if 2 * x + y < k:
            break
        if k % 2 == 0 and 2 * x >= k:
            cx = k // 2
            cy = 0
        elif k % 2 == 0 and 2 * x < k:
            cx = x
            cy = k - 2 * cx
        elif k % 2 and y:
            cx = k // 2
            cy = 1
        elif k % 2 and y == 0:
            cx = k // 2 + 1
            cy = 0
        y -= cy
        x -= cx
        cnt += 1
    print(cnt)


main()
