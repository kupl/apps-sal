import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None] * T
for qu in range(T):
    n, m = map(int, readline().split())
    Ans[qu] = -((-n * m) // 2)
print('\n'.join(map(str, Ans)))
