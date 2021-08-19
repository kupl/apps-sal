from collections import Counter
import sys
input = sys.stdin.readline
Q = int(input())
for testcases in range(Q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    L = len(s)
    ind = 0
    for te in t:
        if te == s[ind]:
            ind += 1
        if ind == L:
            break
    if ind != L:
        print('NO')
        continue
    C = Counter(s) + Counter(p)
    CT = Counter(t)
    for ct in CT:
        if CT[ct] > C[ct]:
            print('NO')
            break
    else:
        print('YES')
