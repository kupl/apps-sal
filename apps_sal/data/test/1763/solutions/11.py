import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('E.txt').readlines())

    def input():
        return next(f)
else:
    def input(): return sys.stdin.readline().strip()

fprint = lambda *args: print(*args, flush=True)

N, A, R, M = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H)

M = min(M, A + R)


def calc(height):
    for cur in range(len(H)):
        if H[cur] >= height:
            break
    if H[cur] < height:
        cur += 1

    up, down = 0, 0
    # print(height, cur, N, H[cur], H)
    for h in H[:cur]:
        down += (height - h)
    for h in H[cur:]:
        up += (h - height)

    if up >= down:
        return down * M + (up - down) * R
    else:
        return up * M + (down - up) * A

# print(calc(8))


# print(Hs)
l, r = 0, max(H) + 1
while l + 1 < r:
    cur = (l + r) // 2
    if calc(cur) < calc(cur + 1):
        r = cur
    else:
        l = cur
# print(l, r)
# print(calc(l), calc(r))
print(min(calc(l), calc(r)))
