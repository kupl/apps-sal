n = int(input())
a = [int(x) for x in input().split()]
r = [x == y for x, y in zip((t + k for t, k in zip(a[:-2], a[1:-1])), a[2:])]
ans = 2
if len(a) < 3:
    print(len(a))
    return
ptr = 0
while ptr < n:
    last = ptr
    while ptr + 2 < n and r[ptr]:
        ptr += 1
    ans = max(ans, ptr - last + 2)
    ptr += 1
print(ans)
