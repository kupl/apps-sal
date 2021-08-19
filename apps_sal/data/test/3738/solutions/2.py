def minus_two(x, y):
    return [x[0] - y[0], x[1] - y[1]]


def will_reach(loc, commands):
    new_loc = [0, 0]
    possible_locs = [[0, 0]]
    for c in commands:
        if c == 'U':
            new_loc[1] += 1
        elif c == 'D':
            new_loc[1] -= 1
        elif c == 'R':
            new_loc[0] += 1
        elif c == 'L':
            new_loc[0] -= 1
        possible_locs += [list(new_loc)]
    all_destinations = [minus_two(loc, pl) for pl in possible_locs]
    for destination in all_destinations:
        realdx = destination[0]
        realdy = destination[1]
        reqdx = new_loc[0]
        reqdy = new_loc[1]
        if destination == [0, 0]:
            return True
        if reqdx != 0 and realdx != 0:
            if realdy / realdx == reqdy / reqdx and (realdy > 0 and reqdy > 0 or (realdy < 0 and reqdy < 0)) and (realdy / reqdy == int(realdy / reqdy)) and (realdx / reqdx == int(realdx / reqdx)):
                return True
        if realdy == reqdy and realdx == reqdx:
            return True
        if reqdx == 0 and realdx == 0:
            if (reqdy > 0 and realdy > 0 or (reqdy < 0 and realdy < 0)) and realdy / reqdy == int(realdy / reqdy):
                return True
        if reqdy == 0 and realdy == 0:
            if (reqdx > 0 and realdx > 0 or (reqdx < 0 and realdx < 0)) and realdx / reqdx == int(realdx / reqdx):
                return True
    return False


def will_reach2(loc, commands):
    new_loc = [0, 0]
    available_loc = []
    for c in commands:
        if c == 'U':
            new_loc[1] += 1
        elif c == 'D':
            new_loc[1] -= 1
        elif c == 'R':
            new_loc[0] += 1
        elif c == 'L':
            new_loc[0] -= 1
        available_loc += [new_loc]
    realdx = new_loc[0]
    realdy = new_loc[1]
    reqdx = loc[0]
    reqdy = loc[1]
    print('realdx', realdx)
    print('realdy', realdy)
    print('reqdx', reqdx)
    print('reqdy', reqdy)
    if reqdx != 0 and realdx != 0:
        return realdy / realdx == reqdy / reqdx
    elif reqdx == 0 and realdx == 0:
        return reqdy / realdy > 0
    else:
        return False


def main():
    first_line = input()
    first_line = first_line.split()
    loc = [int(first_line[0]), int(first_line[1])]
    cmds = input()
    if will_reach(loc, cmds):
        print('Yes')
    else:
        print('No')


main()
