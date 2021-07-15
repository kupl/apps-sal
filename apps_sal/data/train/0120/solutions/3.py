import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None]*T
def calc(d):
    return d*(d+1)//2

for qu in range(T):
    N, M = list(map(int, readline().split()))
    seg = M+1
    leng = N-M
    Ans[qu] = calc(N) - calc(leng//seg) * (seg-leng%seg) - calc(leng//seg+1) *(leng%seg)
    
print('\n'.join(map(str, Ans)))

