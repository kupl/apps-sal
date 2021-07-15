import os
from io import BytesIO, StringIO
#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

DEBUG = False
debug_print = print if DEBUG else lambda *x,**y: None

def input_as_list():
    return list(map(int, input().split()))

def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

def main():
    from collections import defaultdict

    n = int(input())
    vowels = 'aeiou'

    def parse(s):
        count = 0
        last_vowel = ''

        for c in s:
            if c in vowels:
                count += 1
                last_vowel = c

        return count, last_vowel


    alls = []
    pool = defaultdict(dict)
    poolA = []
    poolB = []

    for _ in range(n):
        alls.append(input())

    for s in alls:
        c, lv = parse(s)

        if lv in pool[c]:
            s2 = pool[c].pop(lv)
            poolB.append((s, s2))
        else:
            pool[c][lv] = s

    for d in pool.values():
        d = [s for s in d.values()]
        while len(d) >= 2:
            poolA.append((d.pop(), d.pop()))

    debug_print(poolA, poolB, n)

    out = []
    while poolB:
        s2, s4 = poolB.pop()
        if poolA:
            s1, s3 = poolA.pop()
        else:
            if poolB:
                s1, s3 = poolB.pop()
            else:
                break
        out.append(s1 + ' ' + s2 + '\n' + s3 + ' ' + s4)

    print(len(out))
    print('\n'.join(out))

main()
