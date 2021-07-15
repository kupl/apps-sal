n = int(input())
alst = list(map(int, input().split()))

total = alst[0]
xor = alst[0]
ans = 0
l = 0
r = 0
while 1:
    if xor == total:
        ans += r - l + 1
        r += 1
        if r == n:
            break
        total += alst[r]
        xor ^= alst[r]
    else:
        total -= alst[l]
        xor ^= alst[l]
        l += 1
print(ans)
