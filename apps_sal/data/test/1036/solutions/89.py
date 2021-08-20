def janken(h1, h2):
    handdet = (h2 - h1) % 3
    if handdet == 1:
        return h2
    else:
        return h1


def jankenOnce(handls):
    wonhand = []
    L = len(handls)
    for pair in range(L // 2):
        wonhand.append(janken(handls[2 * pair], handls[2 * pair + 1]))
    return wonhand


def getWinner(handls):
    if len(handls) % 2 == 1:
        return handls
    else:
        winnersList = jankenOnce(handls)
        return getWinner(winnersList)


(n, k) = [int(hoge) for hoge in input().split()]
S = input()
hands = []
for s in S:
    if s == 'R':
        hands.append(0)
    elif s == 'P':
        hands.append(1)
    elif s == 'S':
        hands.append(2)
if n % 2:
    n *= 2
    hands = hands + hands
newhands = hands
for i in range(k):
    newhands = jankenOnce(newhands)
    newhands += newhands
JK = ['R', 'P', 'S']
print(JK[newhands[0]])
