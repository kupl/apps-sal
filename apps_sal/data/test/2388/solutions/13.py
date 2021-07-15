mod = 998244353

n = 0
x = []
d = []

def search(s):
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if s > x[mid]:
            lo = mid + 1
        elif s < x[mid]:
            hi = mid - 1
        else:
            return mid
    return max(lo, hi)


def __starting_point():
    xd = []
    n = int(input())
    for i in range(n):
        xi, di = map(int, input().split())
        xd.append((xi, di))

    xd.sort()
    x = list(map(lambda x: x[0], xd))
    d = list(map(lambda x: x[1], xd))

    dp = [0] * (n+1)
    dp[-1] = 1
    next = [0] * n

    st = []
    st.append((n, 2e9))

    for i in range(n-1, -1, -1):

        while st[-1][1] < x[i] + d[i]:
            st.pop()
        next[i] = st[-1][0]
        st.append((i, x[i]))

    for i in range(n - 1, -1, -1):
        dp[i] = (dp[next[i]] + dp[i + 1]) % mod
    
    print(dp[0])
__starting_point()
