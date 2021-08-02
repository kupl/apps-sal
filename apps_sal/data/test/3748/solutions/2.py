def check(field):
    tr = list(map(''.join, list(zip(*field))))
    paired = set()
    center = -1
    for i, col1 in enumerate(tr):
        if i in paired:
            continue
        for j, col2 in enumerate(tr[i + 1:], start=i + 1):
            if j in paired:
                continue
            if col1 == col2[::-1]:
                paired.add(i)
                paired.add(j)
                break
        else:
            if center == -1 and col1 == col1[::-1]:
                center = i
            else:
                return False
    return True


def arrange_row(field, new_field, i, remain):
    if len(remain) == 0:
        return check(new_field)
    j = remain.pop()
    new_field[i] = field[j]
    for k in list(remain):
        remain.remove(k)
        new_field[h - i - 1] = field[k]
        result = arrange_row(field, new_field, i + 1, remain)
        if result:
            return True
        remain.add(k)
    remain.add(j)
    return False


def solve(h, w, field):
    new_field = [None] * h
    remaining_row = set(range(h))

    if h % 2 == 0:
        return arrange_row(field, new_field, 0, remaining_row)

    for i in list(remaining_row):
        remaining_row.remove(i)
        new_field[h // 2] = field[i]
        result = arrange_row(field, new_field, 0, remaining_row)
        if result:
            return True
        remaining_row.add(i)
    return False


h, w = list(map(int, input().split()))
field = [input() for _ in range(h)]
print(('YES' if solve(h, w, field) else 'NO'))
