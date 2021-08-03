from math import ceil
import sys
def input(): return sys.stdin.readline().strip()


def mismatch(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    check = ''
    for i in range(ceil((k + 2) / 3)):
        check += 'RGB'
    ls = []
    for i in range(3):
        ls.append(check[i:i + k])
    s = input()
    m = n
    for i in range(n - k + 1):
        for j in ls:
            m = min(m, mismatch(s[i:i + k], j))
    print(m)
