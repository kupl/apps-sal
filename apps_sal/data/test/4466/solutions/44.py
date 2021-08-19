(x, y, z) = map(int, input().split())
n = [i for i in range(z, x - z, y + z)]
if n[-1] + y + z <= x:
    print(len(n))
else:
    print(len(n) - 1)
