def jump(n, d, s):
    string = ''
    for x in range(d):
        string += '0'
    for i in range(len(s) - d):
        if s[i:i + d] == string:
            return -1
    count = 0
    dist = 1
    a = 0
    r = 1
    while dist < len(s):
        if d + a < len(s):
            if int(s[d + a]) == 1:
                dist += d
                count += 1
                a += d
            else:
                while d - r > 0:
                    if int(s[d + a - r]) == 1:
                        dist += d - r
                        count += 1
                        a += d - r
                        r = 1
                        break
                    else:
                        r += 1
        else:
            a -= 1
    return count


def __starting_point():
    [n, d] = [int(i) for i in input().split(' ')]
    s = input()
    print(jump(n, d, s))


__starting_point()
