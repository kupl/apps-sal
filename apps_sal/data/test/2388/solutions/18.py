#input
N = int(input())
XD = []
for _ in range(N):
    x, d = list(map(int, input().split()))
    XD.append((x, x+d))

MOD = 998244353

# process
XD.sort(reverse=True)

sei = [(10**9, 0)]
pattern = [0]*(N+1)
pattern[0] = 1
for i, (s, e) in enumerate(XD):
    ei = i
    while e > sei[-1][0]:
        _, ei = sei.pop()
    sei.append((s, ei))
    pattern[i+1] = (pattern[i] + pattern[ei]) % MOD

# output
print((pattern[-1]))

