import sys
input = sys.stdin.readline

def main():
    n = int(input())
    c = list(map(int, input().split()))
    mod = pow(10, 9) + 7
    
    c.sort(reverse=True)
    
    ans = 0
    
    for i in range(n):
        ans += (i+2) * c[i]
        ans %= mod
    
    ans *= pow(2, n*2-2, mod)
    ans %= mod
    
    print(ans)
    
    
def __starting_point():
    main()

__starting_point()
