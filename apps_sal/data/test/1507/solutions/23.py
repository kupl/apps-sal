n, k = [int(i) for i in input().split(' ')]
guests = input()
flag = 'NO'

guards = [' '] * k

for i in range(0, n):
    if guests[i] in guards:
        continue
    if ' ' in guards:
        guards[guards.index(' ')] = guests[i]
        continue
    rest_guests = guests[i:]
    flag = 'YES'
    for g in guards:
        if g in rest_guests:
            continue
        else:
            guards[guards.index(g)] = guests[i]
            flag = 'NO'
    if flag == 'YES':
        break
print(flag)
