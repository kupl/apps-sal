t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    b = int(l[1])
    z = abs(a - b)
    print((z + 9) // 10)
