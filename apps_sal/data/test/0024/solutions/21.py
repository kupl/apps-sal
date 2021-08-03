
def is_in_row(field):
    for s in field:
        for i in range(len(s) - 4):
            if s[i:i + 5].count('X') == 4 and s[i:i + 5].count('.') == 1:
                print('YES')
                return True
    return False


def is_in_col(field):
    for s in [''.join(x) for x in zip(*field)]:
        for i in range(len(s) - 4):
            if s[i:i + 5].count('X') == 4 and s[i:i + 5].count('.') == 1:
                print('YES')
                return True
    return False


def is_in_diag(field):
    shift = []
    for i in range(len(field)):
        shift.append(field[i][i:])
        shift[-1] += 'O' * (10 - len(shift[-1]))

    for s in [''.join(x) for x in zip(*shift)]:
        for i in range(len(s) - 4):
            if s[i:i + 5].count('X') == 4 and s[i:i + 5].count('.') == 1:
                print('YES')
                return True

    shift = []
    for i in range(len(field)):
        shift.append(field[i][:i][::-1])
        shift[-1] += 'O' * (10 - len(shift[-1]))

    for s in [''.join(x) for x in zip(*shift)]:
        for i in range(len(s) - 4):
            if s[i:i + 5].count('X') == 4 and s[i:i + 5].count('.') == 1:
                print('YES')
                return True
    return False


field = [input() for _ in range(10)]

if is_in_row(field):
    return
if is_in_col(field):
    return
if is_in_diag(field):
    return
if is_in_diag(list([x[::-1] for x in field])):
    return

print('NO')
