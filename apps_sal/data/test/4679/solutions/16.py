Sa = list(input())
Sb = list(input())
Sc = list(input())
turn = Sa
ans = 'A'
while turn != []:
    card = turn[0]
    turn.pop(0)
    if card == 'a':
        turn = Sa
        ans = 'A'
    elif card == 'b':
        turn = Sb
        ans = 'B'
    else:
        turn = Sc
        ans = 'C'
print(ans)
