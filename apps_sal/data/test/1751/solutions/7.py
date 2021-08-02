import sys
input = sys.stdin.readline

N = int(input())

MOD = 10**9 + 7

start = 1
to_remove = 1
for i in range(1, N + 1):
    start = (start * i) % MOD
    if i > 1:
        to_remove = (to_remove * 2) % MOD
    # print(start, to_remove)
res = (start - to_remove) % MOD
print(res)
