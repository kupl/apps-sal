import sys

input = sys.stdin.readline
N = int(input())
K = int(input())

c = 0
tmp = 1
while c < N:
    if tmp < K:
        tmp *= 2
    else:
        tmp += K
    c += 1
    # print(tmp)

print(tmp)
