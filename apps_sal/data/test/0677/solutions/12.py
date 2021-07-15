n = int(input())
for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    if a<=c <=b:
        print((b//c+1)*c)
    else:
        print(c)
