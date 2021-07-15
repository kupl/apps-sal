import sys

def __starting_point():
    n = input().split()
    n, m = int(n[0]), int(n[1])
    _l = list()
    for _ in range(n):
      _l.append(input())
    _ms = [int(x) - 1 for x in input().split()]
    common = list(_l[_ms[0]])
    reqlen = len(common)
    for indx in _ms[1:]:
        curr = _l[indx]
        clen = len(curr)
        if clen != reqlen:
            print('No')
            return
        for i in range(len(curr)):
            if curr[i] != common[i]:
                common[i] = '?'
    for i in range(len(_l)):
        if i not in _ms:
            curr = _l[i]
            if len(curr) != reqlen:
                continue
            good = False
            for j in range(reqlen):
                if common[j] == '?':
                    continue
                if common[j] != curr[j]:
                    good = True
            if not good:
                print('No')
                return
    print('Yes')
    print(''.join(common))
__starting_point()
