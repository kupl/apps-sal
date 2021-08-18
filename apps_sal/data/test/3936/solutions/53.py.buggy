# template
def inputlist(): return [int(j) for j in input().split()]
# template


mod = 10**9 + 7

N = int(input())

if N == 1:
    print((3))
    return

S1 = list(input())
S2 = list(input())

blocks = []
s = S1[0]
for i in range(1, N):
    if S1[i] == S1[i - 1]:
        s += S1[i]
    else:
        blocks.append(s)
        s = S1[i]
    if i == N - 1:
        blocks.append(s)

n = len(blocks)

last_blocks = [0] * n

for i in range(1, n):
    last_blocks[i] = len(blocks[i - 1])

ans = 1
for i in range(n):
    tmp = blocks[i]
    last_block = last_blocks[i]
    if last_block == 0:
        if len(tmp) == 1:
            ans *= 3
        else:
            ans *= 6
    if last_block == 1:
        ans *= 2
    if last_block == 2:
        if len(tmp) == 1:
            ans *= 1
        if len(tmp) == 2:
            ans *= 3
    ans %= mod

print((ans % mod))
