N,K = map(int,input().split())
a = list(map(int,input().split()))

def f(N,K,a):
    a.sort()
    if a[0] >= K:
        print(0)
        return

    a = [a[i] for i in range(N) if a[i]<K]
    N = len(a)
    ans = N
    dp = [False]*K
    dp[0] = True
    Smax = 0
    for i,a_ in reversed(list(enumerate(a))):
        if Smax + a_ >= K:
            ans = i
        updated = True
        for j in range(min(Smax,K-a_-1),-1,-1):
            if dp[j]:
                dp[j+a_]=True
                if updated:
                    Smax = max(Smax,j+a_)
                    updated = False
    return ans

print(f(N,K,a))
