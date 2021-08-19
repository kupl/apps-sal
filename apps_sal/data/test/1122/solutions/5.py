(N, M) = (int(_) for _ in input().split())
if N % 2 == 0:
    s = (N - 1) // 4 + 1
    ret = []
    for i in range(1, s):
        ret.append((i, N - i))
    for i in range(s, N // 2):
        ret.append((i, N - i - 1))
else:
    ret = []
    for i in range(1, N // 2 + 1):
        ret.append((i, N - i))
for (r0, r1) in ret[:M]:
    print((r0, r1))
