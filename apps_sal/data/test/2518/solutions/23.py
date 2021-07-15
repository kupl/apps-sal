n, a, b = map(int, input().split())
h_s = [int(input()) for _ in range(n)]

l = (min(h_s) - 1) // a + 1
r = (max(h_s) - 1) // b + 1

c = a - b
while l != r:
    pos = (l + r) // 2
    cnt = 0
    base = b * pos
    for h in h_s:
        rem = h - base
        cnt += max(0, (rem - 1) // c + 1)
    if cnt <= pos:
        r = pos
    else:
        l = pos + 1
print(r)
