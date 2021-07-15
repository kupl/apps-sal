def divisor(n):
    i = 1
    res = []
    while i*i <= n:
        if n%i == 0:
            res.append(i)
            if n//i not in res:
                res.append(n//i)
        i += 1
    res.sort()
    return res

def main():
    n, m = map(int, input().split())
    md = divisor(m)
    ans = 0
    for i in md:
        if (m - n*i)%i == 0 and (m - n*i) >= 0:
            ans = i
        else:
            break
    print(ans)

def __starting_point():
    main()
__starting_point()
