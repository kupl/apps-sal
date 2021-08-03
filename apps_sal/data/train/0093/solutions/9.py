for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    topmost = set()
    a = iter(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for bi in b:
        if bi in topmost:
            k = 0
            topmost.remove(bi)
        else:
            k = len(topmost)
            for ai in a:
                if ai == bi:
                    break
                topmost.add(ai)
                k += 1
            else:
                raise ValueError(f'No {bi} in a')
        ans += 2 * k + 1
    print(ans)
