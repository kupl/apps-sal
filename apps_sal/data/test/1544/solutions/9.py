def pol(n,k):
    ans = 1
    for i in range(k):
        ans *= (n-i)/(i+1)
    k = int(ans)
    if abs(k - ans) < 1/2:
        return k
    return k + 1
n = int(input())
pr = pol(n + 2,3) * pol(n+4,5)
print(pr)
