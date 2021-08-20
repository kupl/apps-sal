n = int(input())
l = list(map(int, input().split()))
chest = 0
biceps = 0
back = 0
for i in range(1, n + 1):
    if i % 3 == 1:
        chest += l[i - 1]
    elif i % 3 == 2:
        biceps += l[i - 1]
    else:
        back += l[i - 1]
if chest >= biceps and chest >= back:
    print('chest')
elif biceps >= chest and biceps >= back:
    print('biceps')
else:
    print('back')
