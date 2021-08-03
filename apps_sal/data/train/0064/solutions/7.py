for _ in range(int(input())):
    n, l = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ls, rs, lx, rx, li, ri = 1, 1, 0, l, 0, n
    total = 0
    while li != ri:
        if (arr[li] - lx) / ls < (rx - arr[ri - 1]) / rs:
            total += (arr[li] - lx) / ls
            rx -= (arr[li] - lx) / ls * rs
            lx = arr[li]
            li += 1
            ls += 1
        else:
            total += (rx - arr[ri - 1]) / rs
            lx += (rx - arr[ri - 1]) / rs * ls
            rx = arr[ri - 1]
            ri -= 1
            rs += 1
    total += (rx - lx) / (ls + rs)
    print(total)
