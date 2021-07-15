__author__ = 'Данила'
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

def solve(x,y,z):
    if y**2 - 4*z*x < 0:
        return -10**27
    else:
        disi = y**2 - 4*z*x
        return min(abs((-y + disi**.5)/2*x), abs((-y - disi**.5)/2*x))

if a*d-b*c == 0:
    print(0)
else:
    det = a*d - b*c
    k = max(a + d + b + c, a - d + c - b, a - d - c + b, a + d - b - c, -a + d - b + c, -a + d - c + b, -a - d + b + c, -a - b - c - d)
    a1 = abs(det/k)
    ans = a1
    print(ans)



