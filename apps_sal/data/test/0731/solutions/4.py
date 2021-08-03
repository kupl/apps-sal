3


def readln(): return tuple(map(int, input().split()))


w, m, k = readln()
s = 1
ans = 0
while w:
    while m >= 10 ** s:
        s += 1
    cnt = 10 ** s - m
    if cnt * s * k <= w:
        ans += cnt
        w -= cnt * s * k
        m = 10 ** s
    else:
        ans += w // (s * k)
        w = 0
print(ans)
