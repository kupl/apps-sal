import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
B = 20
table = [0]*B
for a in A:
    for i in range(B):
        if (1<<i) & a:
            table[i] += 1

ans = 0

for _ in range(N):
    res = 0
    for i in range(B):
        if table[i]:
            table[i] -= 1
            res |= (1<<i)
    ans += res**2

print(ans)
