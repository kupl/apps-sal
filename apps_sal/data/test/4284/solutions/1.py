def main():
    import sys
    input = sys.stdin.readline
    
    def solve():
        k, n, a, b = map(int, input().split())
        
        if k <= n * b:
            print(-1)
            return
        
        l = 0
        r = n + 1
        while r - l != 1:
            m = l + r >> 1
            K = k - a * m
            if K <= 0 or K <= b * (n - m):
                r = m
            else:
                l = m
        print(l)
    
    for _ in range(int(input())):
        solve()
    
    return 0

main()
