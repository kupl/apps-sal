def main():
    import sys
    input = sys.stdin.readline
    
    def okay(n):
        cnt = [0] * 10
        while n:
            cnt[n % 10] += 1
            n //= 10
        if max(cnt) > 1:
            return 0
        return 1
    
    l, r = list(map(int, input().split()))
    
    for i in range(l, r + 1):
        if okay(i):
            print(i)
            return 0
    
    print(-1)
    return 0

main()

