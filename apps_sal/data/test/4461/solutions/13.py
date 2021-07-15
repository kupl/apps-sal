import sys
H, W = map(int,input().split())
if H % 3 == 0 or W % 3 == 0:
    print(0)
    return
def solve(p, q):
    r = int(p / 2)
    s = int(q / 3)
    a, b, c = p*s, r*(q-s), (p-r)*(q-s)
    ans = max(a, b, c) - min(a, b, c)
    a, b, c = p*(s+1), r*(q-s-1), (p-r)*(q-s-1)
    ans = min(ans, max(a, b, c) - min(a, b, c))
    return ans
ans = min(W, H, solve(H, W), solve(W, H))
print(ans)
