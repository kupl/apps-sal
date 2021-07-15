import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None]*T
for qu in range(T):
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    K -= 1
    ma = max(A)
    A = [ma - a for a in A]
    if K & 1:    
        ma = max(A)
        A = [ma - a for a in A]
    Ans[qu] = ' '.join(map(str, A))
print('\n'.join(Ans))
