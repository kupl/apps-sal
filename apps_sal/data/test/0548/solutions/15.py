n = int(input())
l = input()
l = [int(i) for i in l.split()]
d = sum(l)
if d % 2 == 1:
    print('First')
else:
    for i in range(n - 1, -1, -1):
        d -= l[i]
        if d % 2 == 1:
            print('First')
            d = -1
            break
    if d != -1:
        print('Second')
