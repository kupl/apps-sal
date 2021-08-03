n = int(input())
a = list(map(int, input().split()))
a.reverse()
aa = a + a
r = 1
l = 0
ans = -1
while r < 2 * n:
    while r < 2 * n:
        if aa[r - 1] < aa[r]:
            break
        r += 1
    if r - l >= n:
        ans = l
        break
    l = r
    r += 1
print(ans)
