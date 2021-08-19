# Project name: CF-481-E-D3

n, w = map(int, input().split())
a = list(map(int, input().split()))
r = [0]
for i in a:
    r += [r[-1] + i]

if (((w - max(r) + 1) + min(r))) < 0:
    print(0)
else:
    print((w - max(r) + 1) + min(r))
