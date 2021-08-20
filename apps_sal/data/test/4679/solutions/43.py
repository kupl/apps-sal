card = {c: list(input()) for c in 'abc'}
s = 'a'
while card[s]:
    s = card[s].pop(0)
print(s.upper())
