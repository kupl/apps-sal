def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    
    if s % 3 != 0 or len(a) < 3:
        print(0)
        return

    _s = s // 3
    sums = [0] * (n+1)
    ss = 0
    for i in range(n-1, 1, -1):
        ss += a[i]
        sums[i] = sums[i+1] + int(ss == _s)

    res = 0
    ss = 0 
    for i in range(n-2):
        ss += a[i]
        if ss == _s:
            res += sums[i+2]
    print(res)
            

def __starting_point():
    main()


__starting_point()
