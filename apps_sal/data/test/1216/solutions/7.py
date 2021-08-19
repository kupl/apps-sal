def end(r, curr_s, curr_l):
    if curr_l == 0:
        return
    if (curr_s == 'o' or curr_s == 'e') and curr_l == 2:
        r.append(curr_s * 2)
    else:
        r.append(curr_s)


def main():
    n = int(input())
    s = input()
    glasnie = 'aeiouy'
    curr_s = ''
    curr_l = 0
    r = []
    for e in s:
        if e in glasnie:
            if e != curr_s:
                end(r, curr_s, curr_l)
                curr_s = e
                curr_l = 1
            else:
                curr_l += 1
        else:
            end(r, curr_s, curr_l)
            r.append(e)
            curr_s = ''
            curr_l = 0
    end(r, curr_s, curr_l)
    print(''.join(r))


def __starting_point():
    main()


__starting_point()
