SA = input()
SB = input()
SC = input()
S = {'a': SA, 'b': SB, 'c': SC}
card = S['a'][0]
while True:
    if S[card] == '':
        print(card.upper())
        break
    S[card], card = S[card][1:], S[card][0]
