import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [1]*T
for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().strip()))
    Aodd = [A[i]%2 for i in range(N) if not i&1]
    Aeven = [A[i]%2 for i in range(N) if i&1]
    if len(Aodd) == len(Aeven):
        if all(a == 1 for a in Aeven):
            continue
        else:
            Ans[qu] = 2
    else:
        if all(a == 0 for a in Aodd):
            Ans[qu] = 2

print('\n'.join(map(str, Ans)))
