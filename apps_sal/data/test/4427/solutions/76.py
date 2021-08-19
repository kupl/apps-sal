(r, D, x) = map(int, input().split())
c = 0
while c < 10:
    x = r * x - D
    print(x)
    c += 1
