n, h, k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
ans = 0
rem = 0
i = 0
while i < n:
    while rem <= h and i < n:
        rem += A[i]
        i += 1
    if rem > h:
        i -= 1
        rem -= A[i]
    ans += rem // k
    rem %= k
    if i < n and rem + A[i] > h:
        ans += 1
        rem = 0
if rem > 0:
    ans += 1
print(ans)
