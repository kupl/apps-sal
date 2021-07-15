#!/usr/bin/env python3

def main():
    from   collections import Counter
    import re

    try:
        while True:
            s = input()
            d = Counter()
            for i in range(4):
                t = s[i::4]
                d[re.search(r"[^!]", t).group()] = t.count('!')

            print(d['R'], d['B'], d['Y'], d['G'])

    except EOFError:
        pass

main()

