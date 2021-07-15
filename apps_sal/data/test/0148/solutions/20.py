n, a, x, b, y = [int(x) for x in input().split()]

ar = []
br = []

if a < x:
    ar = list(range(a, x+1))
else:
    ar = list(range(a, n+1)) + list(range(1, x+1))

if b > y:
    br = list(range(b, y-1, -1))
else:
    br = list(range(b, 0, -1)) + list(range(n, y-1, -1))

can = False

for i in range(min(len(ar), len(br))):
    if ar[i] == br[i]:
        can = True

if can:
    print("YES")
else:
    print("NO")
