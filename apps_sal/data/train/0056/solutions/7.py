import sys


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    if k % n == 0:
        print(0)
    else:
        print(2)
    for i in range(n):
        ans = ''
        if i < k % n:
            ans = '1' * (k // n + 1) + '0' * (n - (k // n + 1))
            ans = ans[i:] + ans[:i]
        else:
            ans = '1' * (k // n) + '0' * (n - k // n)
            ans = ans[i:] + ans[:i]
        print(ans)
