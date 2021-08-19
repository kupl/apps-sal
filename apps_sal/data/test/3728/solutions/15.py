__author__ = 'Think'


def parse(row):
    count = 0
    problems = []
    for i in range(1, m + 1):
        if i != row[i - 1]:
            count += 1
            problems.append((i, row[i - 1]))
    if count == 0:
        return [0]
    elif count == 2:
        return [2, sorted((problems[0][0], problems[0][1]))]
    elif count == 3:
        return [3, sorted((problems[0][0], problems[1][0])), sorted((problems[2][0], problems[1][0])), sorted((problems[0][0], problems[2][0]))]
    elif count == 4 and row[problems[0][1] - 1] == problems[0][0]:
        if problems[0][1] != problems[1][0]:
            return [3, sorted((problems[0][0], problems[0][1])), sorted((problems[1][0], problems[1][1]))]
        else:
            return [3, sorted((problems[0][0], problems[0][1])), sorted((problems[2][0], problems[2][1]))]
    else:
        return [4]


def merge(l1, l2):
    if l1[0] == 4 or l2 == [4]:
        return 'Fail'
    elif l1[0] == 0:
        return l2
    elif l2[0] == 0:
        return l1
    elif l1[0] == 3 and l2[0] == 3:
        new = [3]
        for i in l1[1:]:
            if i in l2[1:]:
                new.append(i)
        if len(new) > 1:
            return new
        else:
            return 'Fail'
    elif (l1[0] == 2) != (l2[0] == 2):
        if l1[0] == 2:
            newl2 = l1
            newl3 = l2
        else:
            newl2 = l2
            newl3 = l1
        if len(newl2) == 1:
            return 'Fail'
        if newl2[1] in newl3[1:]:
            return newl2
        else:
            return 'Fail'
    elif l1[0] == 2 and l2[0] == 2:
        if l1 == l2:
            return l1
        else:
            return [2]
    print('Missed a case!', l1, l2)


current = [0]
broken = False
(n, m) = [int(i) for i in input().split()]
for j in range(n):
    newrow = [int(i) for i in input().split()]
    new = parse(newrow)
    current = merge(new, current)
    if current == 'Fail':
        print('NO')
        broken = True
        break
if not broken:
    print('YES')
