import sys


def input():
    return sys.stdin.readline().strip()


T = int(input())
for i in range(T):
    (n, k) = map(int, input().split())
    ls = list(map(int, input().split()))
    odd = 0
    for i in ls:
        if i % 2:
            odd += 1
    if odd - k < 0 or (odd - k) % 2:
        print('NO')
    else:
        print('YES')
        cnt = 0
        for i in range(n):
            if cnt == k - 1:
                break
            if ls[i] % 2:
                print(i + 1, end=' ')
                cnt += 1
        print(n)
