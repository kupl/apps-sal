import bisect


def main():
    N = int(input())
    SS = []
    for _ in range(N):
        SS.append(input())
    S = []
    for s in SS:
        while '()' in s:
            s = s.replace('()', '')
        S.append(s)
    S = [s for s in S if s != '']
    sum_op = 0
    sum_cl = 0
    S_both_op = []
    S_both_cl = []
    for s in S:
        if not ')' in s:
            sum_op += len(s)
        elif not '(' in s:
            sum_cl += len(s)
        else:
            pos = s.find('(')
            if pos <= len(s) - pos:
                S_both_op.append((pos, len(s) - pos))
            else:
                S_both_cl.append((pos, len(s) - pos))

    S_both_op.sort(key=lambda x: x[0])
    S_both_cl.sort(key=lambda x: -x[1])

    for p in S_both_op:
        sum_op -= p[0]
        if(sum_op < 0):
            print('No')
            return
        sum_op += p[1]

    for p in S_both_cl:
        sum_op -= p[0]
        if(sum_op < 0):
            print('No')
            return
        sum_op += p[1]

    if sum_op == sum_cl:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
