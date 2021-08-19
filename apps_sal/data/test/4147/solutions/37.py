n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]


def kadomatsu(li, x):
    cost = 0
    cost += 10 * (len(li) - 1)
    cost += abs(sum(li) - x)
    return cost


ansli = []

for i in range(4**n):
    #print(i,end = " ")
    #memo = i
    amari = []
    while True:
        if i >= 4:
            amari.append(i % 4)
            i = i // 4
        else:
            amari.append(i)
            break
    gyaku = amari[::-1]
    #print(gyaku,end=" ")
    gya = [0] * (n - len(gyaku)) + gyaku
    #print(gya,end = " ")
    al = []
    bl = []
    cl = []
    for j in range(n):
        if gya[j] == 1:
            al += [l[j]]
        elif gya[j] == 2:
            bl += [l[j]]
        elif gya[j] == 3:
            cl += [l[j]]
    if al and bl and cl:
        ans = kadomatsu(al, a) + kadomatsu(bl, b) + kadomatsu(cl, c)
        ansli += [ans]
        # print(memo,gya,al,bl,cl)
print(min(ansli))
