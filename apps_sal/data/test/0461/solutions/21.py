import copy


def solve():
    (n, a, b, c) = [int(input()) for i in range(4)]
    nowloc = 'ab'
    mealed = 1
    totaldistance = 0
    history = ['ab']
    while mealed < n:
        if nowloc == 'ab':
            if a < b:
                nowloc = 'ac'
                totaldistance += a
            else:
                nowloc = 'bc'
                totaldistance += b
        elif nowloc == 'bc':
            if b < c:
                nowloc = 'ab'
                totaldistance += b
            else:
                nowloc = 'ac'
                totaldistance += c
        elif nowloc == 'ac':
            if a < c:
                nowloc = 'ab'
                totaldistance += a
            else:
                nowloc = 'bc'
                totaldistance += c
        history.append(copy.deepcopy(nowloc))
        mealed += 1
    return (totaldistance, history)


print(solve()[0])
