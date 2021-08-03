t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    z = a & b
    print((a ^ z) + (b ^ z))
