(n, x) = map(int, input().split())
z = abs(sum(list(map(int, input().split()))))
if z % x == 0:
    print(z // x)
else:
    print(z // x + 1)
