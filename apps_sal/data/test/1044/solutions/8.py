a = int(input())
b = list(map(int, input().split()))
c = {2: 1, 1: 2}
d = 2
for i in range(a):
    if b[i] == 1:
        print(d)
    else:
        if b[i] % 2 == 0:
            print(c[d])
            d = c[d]
        else:
            print(d)

