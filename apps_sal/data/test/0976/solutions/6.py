def movie():
    (n, x) = [int(i) for i in input().split()]
    ans = 0
    last = 0
    for i in range(n):
        (start, end) = [int(p) for p in input().split()]
        ans += (start - last - 1) % x
        ans += end - start + 1
        last = end
    print(ans)
    return


movie()
