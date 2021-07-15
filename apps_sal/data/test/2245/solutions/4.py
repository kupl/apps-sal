import sys
Q = int(input())
def check(N, k):
    if k % 3:
        return (N % 3 == 0)
    if N%(k+1) == k:
        return False
    return ((N%(k+1)) % 3 == 0)

for _ in range(Q):
    N, k = list(map(int, sys.stdin.readline().split()))
    if check(N, k):
        print('Bob')
    else:
        print('Alice')

