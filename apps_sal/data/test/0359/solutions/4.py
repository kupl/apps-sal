def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


A, H, W = map(int, input().split())
G = gcd(A + H, A + W)
S = (A + W) // G
T = ((W // A + 1) // S) * S - 1
if T <= 0:
    print(-1)
else:
    print("%.10lf" % ((W - T * A) / (T + 1)))
