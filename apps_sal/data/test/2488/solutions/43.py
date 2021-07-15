import sys
input = sys.stdin.readline


n, d, a = list(map(int, input().split()))
fox = [list(map(int, input().split())) for _ in range(n)]

fox.sort()

sub = [0]*(n+1)

def bisect(x):
    l, r = 0, n
    while r-l > 1:
        k = (r+l)//2
        if fox[k][0] <= x:
            l = k
        else:
            r = k
    if fox[l][0] <= x:
        return l
    return r


def main():
    ans = 0
    
    for i in range(n):
        if i != 0:
            sub[i] += sub[i-1]
        if fox[i][1]-a*sub[i] <= 0:
            continue
        count = (fox[i][1]-sub[i]*a-1)//a+1
        ans += count
        sub[i] += count
        sub[bisect(fox[i][0]+2*d)+1] -= count

    print(ans)

    
def __starting_point():
    main()

__starting_point()
