import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None] * T

for qu in range(T):
    N, M = map(int, readline().split())
    ans = 'NO'
    for _ in range(N):
        a, b = map(int, readline().split())
        c, d = map(int, readline().split())
        if b == c:
            ans = 'YES'

    if M & 1:
        Ans[qu] = 'NO'
        continue
    Ans[qu] = ans

print('\n'.join(Ans))
