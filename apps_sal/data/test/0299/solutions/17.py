input()
l = [int(x) for x in input().split()]
a = sum(l[0::3])
b = sum(l[1::3])
c = sum(l[2::3])
if a > b and a > c:
    print('chest')
elif b > a and b > c:
    print('biceps')
else:
    print('back')
