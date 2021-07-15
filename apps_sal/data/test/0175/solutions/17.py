R=lambda:list(map(int,input().split()))

n, m = R()

def pr(a, b):
    if a == 0 or b == 0: return([a,b])
    if a//(2*b) > 0: return(pr(a - a//(2*b) * 2 * b , b))
    if b//(2*a) > 0: return(pr(a, b - b//(2*a) * 2 * a))
    return [a,b]

ans = pr(n, m)

print(ans[0], ans[1])

