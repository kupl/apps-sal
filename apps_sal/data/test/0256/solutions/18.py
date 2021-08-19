a1, d1 = [int(a) for a in input().split()]
a2, d2 = [int(a) for a in input().split()]
a3, d3 = [int(a) for a in input().split()]
a4, d4 = [int(a) for a in input().split()]

# Team 1 wins if E a team 1 st A team 2, team 1 must win
# Team 2 wins if A team 1 E team 2 st team 2 must win

team1win = False
for (A1, D1) in [(a1, d2), (a2, d1)]:
    good = True
    for (A2, D2) in [(a3, d4), (a4, d3)]:
        if A1 <= D2 or D1 <= A2:
            good = False
    if good:
        team1win = True
team2win = True
for (A1, D1) in [(a1, d2), (a2, d1)]:
    good = False
    for (A2, D2) in [(a3, d4), (a4, d3)]:
        if D2 > A1 and A2 > D1:
            good = True
    if not good:
        team2win = False

if team1win:
    print('Team 1')
elif team2win:
    print('Team 2')
else:
    print('Draw')
