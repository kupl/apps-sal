for tt in range(int(input())):
    a, b, c, d = map(int, input().split())
    if(a <= b):
        print(b)
        continue
    a = a - b
    if(d >= c):
        print(-1)
        continue
    val = a // (c - d)
    if(a % (c - d) != 0):
        val += 1
    print(b + val * c)
