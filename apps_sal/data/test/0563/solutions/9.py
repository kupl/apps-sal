from fractions import gcd
def checkok(a, b, c):
    if gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c)!= 1:
        return True
    return False

mark = False
l, r = list(map(int, input().split(' ')))
for i in range(l, r+1):
    for j in range(i+1, r+1):
        for k in range(j+1, r+1):
            if checkok(i, j, k) and not mark:
                print(i, j, k)
                mark = True

if not mark:
    print(-1)


