def main():
    import sys
    input = sys.stdin.readline
	
    m, k = list(map(int, input().split()))
    d = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    t = 0
    f = 0
    ma = 0
    
    for i in range(m):
        f += s[i]
        ma = max(ma, s[i])
        while f < d[i]:
            f += ma
            t += k
        t += d[i]
        f -= d[i]
    
    print(t)
    
    return 0

main()

