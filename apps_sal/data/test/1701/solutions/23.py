a, b = [int(i) for i in input().split()]
dic1 = {}
for _ in range(a):
    n, m = input().split()
    dic1[m] = n
for _ in range(b):
    c, i = input().split()
    print(c + " " + i + "
