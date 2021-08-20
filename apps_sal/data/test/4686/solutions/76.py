import math
from datetime import date


def main():
    s = input()
    a = [0 for i in range(26)]
    for c in s:
        a[ord(c) - ord('a')] += 1
    ok = 'True'
    for i in range(26):
        if a[i] % 2 == 1:
            ok = 'False'
    if ok == 'True':
        print('Yes')
    else:
        print('No')


main()
