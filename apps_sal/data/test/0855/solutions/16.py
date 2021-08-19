def read(): return list(map(int, input().split(' ')))


k, a, b = read()
A = [read() for _ in range(3)]
B = [read() for _ in range(3)]

ra, rb = 0, 0

skipped = False
pos = {(a, b): 0}
scoreA = {(a, b): 0}
scoreB = {(a, b): 0}
if (b - a) % 3 == 1:
    rb = 1
    #scoreB[(a, b)] = rb
elif (b - a) % 3 == 2:
    ra = 1
    #scoreA[(a, b)] = ra

i = 1
while i < k:
    na = A[a - 1][b - 1]
    nb = B[a - 1][b - 1]
    #print('game:', na, nb)

    if (na, nb) in pos and not skipped:
        cycleLen = i - pos[(na, nb)]
        cycleScoreA = ra - scoreA[(na, nb)]
        cycleScoreB = rb - scoreB[(na, nb)]

        skipCycles = (k - i) // cycleLen
        #print('Skip:', cycleLen, cycleScoreA, cycleScoreB, skipCycles)
        ra += cycleScoreA * skipCycles
        rb += cycleScoreB * skipCycles
        i += skipCycles * cycleLen

        skipped = True
    else:
        scoreA[(na, nb)] = ra
        scoreB[(na, nb)] = rb
        pos[(na, nb)] = i

        if (nb - na) % 3 == 1:
            rb += 1
            #print(i, '+b', ra, rb)
        elif (nb - na) % 3 == 2:
            ra += 1
            #print(i, '+a', ra, rb)

        i += 1
        a, b = na, nb

# print('Answer')
print(ra, rb)
# print('ScoreA')
# print(scoreA)
# print('ScoreB')
# print(scoreB)
# print('pos')
# print(pos)
