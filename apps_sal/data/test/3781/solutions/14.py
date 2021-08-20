from collections import Counter


def solve(n, a):
    n %= 2
    c = Counter(a)
    flag = 0
    for k in c.keys():
        if c[k] % 2 == 1:
            flag = 1
            break
    print('First' if flag + n == 1 else 'Second')


T = int(input())
for i in range(T):
    N = int(input())
    (*A,) = map(int, input().split())
    solve(N, A)
