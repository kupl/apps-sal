import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

n_c4 = 0
n_c2 = 0
n_c0 = 0

for ai in a:
    if ai % 4 == 0:
        n_c4 += 1
    elif ai % 2 == 0:
        n_c2 += 1
    else:
        n_c0 += 1
if n_c4 >= n_c0 or (n_c4 == n_c0 - 1 and n_c4 + n_c0 == N):
    print('Yes')
else:
    print('No')
