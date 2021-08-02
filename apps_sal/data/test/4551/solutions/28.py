a = list(map(int, input().split()))
a = a[0] + a[1] - a[2] - a[3]
if a == 0:
    print('Balanced')
elif a > 0:
    print('Left')
else:
    print('Right')
