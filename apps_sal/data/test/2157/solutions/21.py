def solve():
    n, q = list(map(int, input().split()))

    a = list(map(int, input().split()))
    a.sort(reverse=True)

    w = [0 for i in range(n+2)]
    
    for query in range(q):
        l, r = list(map(int, input().split()))
        w[l] += 1
        w[r+1] -= 1

    for i in range(2, n+1):
        w[i] += w[i-1]

    w.sort(reverse=True)

    maxSum = 0
    for i in range(n):
        maxSum += a[i]*w[i]

    print(maxSum)

def __starting_point():
    solve()

__starting_point()
