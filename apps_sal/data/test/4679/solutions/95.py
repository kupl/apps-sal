Sa = list(input())
Sb = list(input())
Sc = list(input())
card = Sa.pop(0)
while True:
    if card == 'a':
        S = Sa
    if card == 'b':
        S = Sb
    if card == 'c':
        S = Sc
    try:
        card = S.pop(0)
    except:
        print(card.upper())
        break
