def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

cntx, cnty, x, y = list(map(int, input().split()))
d = x * y // gcd(x, y)

v = cnt = 0
while (cntx + cnty > cnt):
    dxy = cntx + cnty - cnt
    
    cx = (v + dxy) // x - v // x
    cy = (v + dxy) // y - v // y
    cxy = (v + dxy) // d - v // d

    cnt += dxy - cx - cy + cxy
    cntx -= min(cy - cxy, cntx)
    cnty -= min(cx - cxy, cnty)
    
    v += dxy

print(v)

