def solve(n,a,b,c,d):
    ans = 0
    sums = [a+b, b+d, d+c, c+a]
    minsum = min(sums)
    maxsum = max(sums)
    tmp = minsum + n
    if (tmp <= maxsum):
        return ans
    else:
        ans += n * (tmp - maxsum)
    return ans
    
(n,a,b,c,d) = [int(x) for x in input().split()]
print(solve(n,a,b,c,d))
