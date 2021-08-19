aa = input()
(n, m) = [int(s) for s in aa.split(' ')]
exams = []
res = [0] * n
for i in range(m):
    aa = input()
    (s, d, c) = [int(s) for s in aa.split(' ')]
    el = {'s': s - 1, 'd': d - 1, 'c': c}
    exams.append(el)
    res[d - 1] = m + 1
for i in range(n - 1, -1, -1):
    if res[i] > 0:
        continue
    exam_num = -1
    min_zapas = n + 1
    for j in range(m):
        if exams[j]['s'] <= i and i < exams[j]['d'] and (exams[j]['c'] > 0):
            zapas = i - exams[j]['s'] - exams[j]['c']
            if zapas < min_zapas:
                min_zapas = zapas
                exam_num = j
            if zapas < 0:
                break
    if exam_num == -1:
        continue
    res[i] = exam_num + 1
    exams[exam_num]['c'] = exams[exam_num]['c'] - 1
possible = True
for i in range(m):
    if exams[i]['c'] > 0:
        possible = False
        break
if possible:
    print(' '.join([str(x) for x in res]))
else:
    print(-1)
