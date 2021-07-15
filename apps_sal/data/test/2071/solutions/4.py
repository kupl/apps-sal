
def getss(a):
    n = len(a)
    ps = [0] * (n+1)
    for i in range(n-1,0,-1):
        ps[i] = ps[i+1] + a[i]
    return ps

def getSum(a, b):
    n = len(a)
    ans = 0
    for i in range(n):
        ans += a[i] * i
    for i in range(n, 2*n):
        ans += b[2*n-i-1] * i
    return ans   

def main():
    n, = list(map(int, input().split(' ')))
    a = [x for x in map(int, input().split(' '))]
    b = [x for x in map(int, input().split(' '))]

    if n == 1:
        print(b[0])
        return

    ssa = getss(a)
    ssb = getss(b)
    
    tans = getSum(a, b)
    ans = tans
    for i in range(0, n - 1, 2):
        tans -= (i*2) * a[i] + (i*2+1) * a[i+1] + (2*n-1)*b[i] + (2*n-2)*b[i+1]
        tans += (i*2) * a[i] + (i*2+3) * a[i+1] + (i*2+1)*b[i] + (i*2+2)*b[i+1]
        tans += 2 * ssa[i+2] + 2 * ssb[i+2]
        ans = max(ans, tans)
    
    tans = getSum(b, a)
    tans -= (2*n-1) * a[0]
    tans += b[0]
    tans += ssa[1] + ssb[1]
    ans = max(ans, tans)
    for i in range(1, n - 1, 2):
        tans -= (i*2) * b[i] + (i*2+1) * b[i+1] + (2*n-1)*a[i] + (2*n-2)*a[i+1]
        tans += (i*2) * b[i] + (i*2+3) * b[i+1] + (i*2+1)*a[i] + (i*2+2)*a[i+1]
        tans += 2 * ssa[i+2] + 2 * ssb[i+2]
        ans = max(ans, tans)
    print(ans)

def __starting_point():
    main()

__starting_point()
