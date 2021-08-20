import sys
input = sys.stdin.readline
N = int(input().rstrip('\n'))
As = [int(x) for x in input().rstrip('\n').split()]
res = [0] * N
for i in range(N, 0, -1):
    now = sum(res[i - 1::i]) % 2
    if now != As[i - 1]:
        res[i - 1] += 1
print(sum(res))
print(*[x + 1 for x in range(N) if res[x] > 0])
