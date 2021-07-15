"""
def main():
    n, m = map(int, input().split())
    max = 10 ** 4
    gr = []
    for i in range(max):
        gr.append([0] * max)
    i, j, k, l = 0,0,m,n
    while gr[i][j] != 1
    
def main():
    n, m = map(int, input().split())
    l = 0
    while n != m:
        if n >= m:
            l += n-m
            n = m
        else:
            if m % 2:
                l += 1
                m += 1
            else:
                if m // 2 <= n:
                    l += 1 + n - m //2
                    n = m
                else:
                    n *= 2
                    l += 1
    print(l)
"""
def main():
    n, m = list(map(int, input().split()))
    print(rec(n,m))
def rec(n,m):
    if m <= n:
        return n-m
    else:
        if m % 2:
            return rec(n,m+1)+1
        else:
            return rec(n, m // 2) + 1
def __starting_point():
    main()

__starting_point()
