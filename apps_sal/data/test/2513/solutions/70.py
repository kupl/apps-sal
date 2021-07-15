def convert(s):
    if s == 'S' or s == 'o':
        return 1
    else:
        return -1


n = int(input())
s = input()

cands = [['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']]

for cand in cands:
    for i in range(1, len(s)-1):
        if cand[-1] == 'S':
            if s[i] == 'o' and cand[-2] == 'S':
                cand.append('S')
            elif s[i] == 'x' and cand[-2] == 'S':
                cand.append('W')
            elif s[i] == 'o' and cand[-2] == 'W':
                cand.append('W')
            else:
                cand.append('S')
        else:
            if s[i] == 'o' and cand[-2] == 'S':
                cand.append('W')
            elif s[i] == 'x' and cand[-2] == 'S':
                cand.append('S')
            elif s[i] == 'o' and cand[-2] == 'W':
                cand.append('S')
            else:
                cand.append('W')
    if (convert(cand[0]) * convert(cand[-1]) * convert(cand[1]) * convert(s[0]) == 1) and \
            (convert(cand[0]) * convert(cand[-1]) * convert(cand[-2]) * convert(s[-1]) == 1):
        print((''.join(cand)))
        return

print((-1))

