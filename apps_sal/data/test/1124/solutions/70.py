def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while x % y > 0:
        x, y = y, x % y
    return y
    

N = int(input())
A = list(map(int, input().split()))
r = A[0]

for a in A[1:]:
    r = gcd(r, a)
print(r)

