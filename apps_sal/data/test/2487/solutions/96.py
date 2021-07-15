def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input())
    edges = 0
    for i in range(n-1):
        u, v = map(int, input().split())
        edges += min(u, v)*(n-max(u, v)+1)
    ans = n*(n+1)*(n+2)//6 - edges
    print(ans)

def __starting_point():
    main()
__starting_point()
