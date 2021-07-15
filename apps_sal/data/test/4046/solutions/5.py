def __starting_point():
    n = input()
    a = list(map(int, input().split()))
    b = [0]
    for ai in a:
        b.append(b[-1] + ai)
    b.sort()
    
    for i in range(1, len(b)):
        if b[i - 1] + 1 != b[i]:
            print(-1)
            break
    else:
        zero_idx = b.index(0)
        x = zero_idx + 1
        res = [x]
        for ai in a:
            res.append(res[-1] + ai)
        print(' '.join(map(str, res)))

__starting_point()
