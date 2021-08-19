import re
import sys


def g(cts, names):
    la = dict([(p, None) for p in names.difference(cts[0])])
    if len(la) == 0:
        return None
    d = [la]
    for i in range(1, len(cts)):
        prev = d[-1]
        la = dict()
        for p in names.difference(cts[i]):
            for n in prev.keys():
                if n != p:
                    la[p] = n
                    break
        if len(la) == 0:
            return None
        d.append(la)
    cur = list(d[-1].keys())[0]
    result = []
    for i in range(len(cts) - 1, -1, -1):
        result.append(cur)
        cur = d[i][cur]
    result.reverse()
    return result


def solve():
    n = int(input())
    names = input().split()
    set_names = set(names)

    def get_names(text):
        result = []
        for p in re.split('\\W+', text):
            if p in set_names:
                result.append(p)
        return result
    m = int(input())
    messages = []
    for i in range(m):
        s = input()
        colon = s.find(':')
        name = s[:colon]
        text = s[colon + 1:]
        if name == '?':
            name = None
        messages.append([name, text, get_names(text)])
    for i in range(m):
        if messages[i][0]:
            continue
        j = i
        cts = []
        while j < m and (not messages[j][0]):
            cts.append(set(messages[j][2]))
            j += 1
        if i > 0:
            cts[0].add(messages[i - 1][0])
        if j < m:
            cts[-1].add(messages[j][0])
        sb = g(cts, set_names)
        if not sb:
            return None
        for k in range(i, j):
            messages[k][0] = sb[k - i]
    for p in messages:
        print('%s:%s' % (p[0], p[1]))
    return True


def main():
    tests = int(input())
    for i in range(tests):
        if not solve():
            print('Impossible')
    return 0


def __starting_point():
    return main()


__starting_point()
