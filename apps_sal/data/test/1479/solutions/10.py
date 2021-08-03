n, m, k = [int(x) for x in input().split()]
park = [input() for i in range(n)]
answers = [0] * m
for inot in range(n):
    for j in range(m):
        if park[inot][j] != '.':
            i = (j, inot, park[inot][j])
            if i[2] == 'R':
                if i[0] + i[1] < m:
                    answers[i[0] + i[1]] += 1
            elif i[2] == 'L':
                if i[0] - i[1] >= 0:
                    answers[i[0] - i[1]] += 1
            elif i[2] == 'U':
                if not i[1] & 1:
                    answers[i[0]] += 1
for i in answers:
    print(i, end=' ')
