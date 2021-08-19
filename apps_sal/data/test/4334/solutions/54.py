(x, y) = input().split()
(z, w) = map(int, input().split())
u = input()
if x == u:
    print(z - 1, w)
else:
    print(z, w - 1)
