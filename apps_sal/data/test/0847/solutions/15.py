a = [int(i) for i in input().split(" ")]
n = a[0]
maxi = a[1]
a = [int(i) for i in input().split(" ")]
c = 0
s = sum(a)
while s != 0:
    if s <= maxi and s >= -maxi:
        c += 1
        s = 0
    elif s > maxi:
        c += 1
        s -= maxi
    elif s < -maxi:
        c += 1
        s += maxi
print(c)
