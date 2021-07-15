import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None]*T

for qu in range(T):
    N, K = list(map(int, readline().split()))
    A = list(map(int, readline().split()))
    if K == 1:
        if len(set(A)) == 1:
            Ans[qu] = 1
        else:
            Ans[qu] = -1
    else:
        s = len(set(A))        
        if K >= s:
            Ans[qu] = 1
        else:
            Ans[qu] = 1-((K-s)//(K-1))

print('\n'.join(map(str, Ans)))

