def winner(q, r):
    if q == r:
        return 'd'
    if q == 0 and r == 2:
        return 'a'
    if r == 0 and q == 2:
        return 'b'
    if q > r:
        return 'a'
    return 'b'


k, a, b = [int(x) - 1 for x in input().split()]
A = [[int(x) - 1 for x in input().split()] for y in range(3)]
B = [[int(x) - 1 for x in input().split()] for z in range(3)]
score = {'a': 0, 'b': 0, 'd': 0}
score[winner(a, b)] += 1
d = {(a, b): 0}
i = 1
j = -1

while k:
    na = A[a][b]
    nb = B[a][b]
    if (na, nb) in list(d.keys()):
        j = d[(na, nb)]
        break
    else:
        d[(na, nb)] = i
        score[winner(na, nb)] += 1
        a = na
        b = nb
    i += 1
    k -= 1

if j == -1:
    print(score['a'], score['b'])
    return

period = {'a': 0, 'b': 0, 'd': 0}
end_score = {'a': 0, 'b': 0, 'd': 0}

rem = k % (i - j)
per = k // (i - j)

for move in d:
    if d[move] < j:
        continue
    if d[move] < j + rem:
        end_score[winner(move[0], move[1])] += 1
    period[winner(move[0], move[1])] += 1

for win in ['a', 'b', 'd']:
    score[win] += end_score[win] + per * period[win]

# print('rem:', rem, 'per:', per, 'period:', period, 'end score:', end_score)

print(score['a'], score['b'])
