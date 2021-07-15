import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None]*T
for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = [b-a for a, b in zip(A, B)]
    while C and C[-1] == 0:
        C.pop()
    C.reverse()
    while C and C[-1] == 0:
        C.pop()
    
    if not C or (len(set(C)) == 1 and C[0] > 0):
        Ans[qu] = 'YES'
    else:
        Ans[qu] = 'NO'

print('\n'.join(map(str, Ans)))
