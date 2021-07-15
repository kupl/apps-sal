S = dict()
S['Q'] = 9
S['R'] = 5
S['B'] = 3
S['N'] = 3
S['P'] = 1
S['K'] = 0
S['q'] = -9
S['r'] = -5
S['b'] = -3
S['n'] = -3
S['p'] = -1
S['k'] = 0

score = 0
for i in range(8) :
    x = input()
    for j in x :
        if j in S :
            score += S[j]

if score > 0 :
    print("White")
elif score == 0 :
    print("Draw")
else :
    print("Black")

