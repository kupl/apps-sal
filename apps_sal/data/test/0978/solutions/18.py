k = 2*int(input())
l1 = input()
l2 = input()
l3 = input()
l4 = input()
times = [0,0,0,0,0,0,0,0,0]
for cont in range(0,4):
    for tmp in range(1,10):
        if l1[cont] == str(tmp):
            times[tmp-1] += 1
        if l2[cont] == str(tmp):
            times[tmp-1] += 1
        if l3[cont] == str(tmp):
            times[tmp-1] += 1
        if l4[cont] == str(tmp):
            times[tmp-1] += 1

l = True
for tmp in times:
    if tmp > k:
        l = False

if l == True:
    print('YES')
else:
    print('NO')
