S = {}
for i in 'ABC':
    S[i] = [w for w in input()]
ans = ''
judge = True
turn = S['A'].pop(0).upper()
while judge:
    if S[turn] == []:
        ans = turn
        judge = False
    else:
        turn = S[turn].pop(0).upper()
print(ans)
