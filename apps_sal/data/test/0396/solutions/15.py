# read l, r;
a = [int(x) for x in input().split()]
l = a[0]
r = a[1]
#l = int(input())
#r = int(input())
res = 0
for x in range(0, 32):
    for y in range(0, 21):
        if ((((2**x) * (3**y)) >= l) and (((2**x) * (3**y)) <= r)):
            res = res + 1
print(res)
