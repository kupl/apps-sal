n = int(input())
cards = list(map(int, input().split()))
s = True
d = False
ps = 0
pd = 0
while len(cards) > 0:
    if s:
        if cards[0] > cards[-1]:
            ps += cards[0]
            t = 0
        else:
            ps += cards[-1]
            t = -1
        s = False
        d = True
        cards.pop(t)
    elif d:
        if cards[0] > cards[-1]:
            pd += cards[0]
            t = 0
        else:
            pd += cards[-1]
            t = -1
        s = True
        d = False
        cards.pop(t)
print(ps, pd)
