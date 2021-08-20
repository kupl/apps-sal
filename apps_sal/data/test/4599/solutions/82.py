n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
a = 0
b = 0
zyu = 0
for i in l:
    if zyu == 0:
        a += i
        zyu = 1
    else:
        zyu = 0
        b += i
if a < b:
    print(b - a)
elif a > b:
    print(a - b)
else:
    print('0')
