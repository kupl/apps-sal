N = int(input())
A = list(map(int, input().split()))

xo = A[0]
l = 0
r = 1
ans = 0

while l < N:
    if r == N:
        ans += r - l
        l += 1
        continue
    if xo ^ A[r] == xo + A[r]:
        xo += A[r]
        r += 1
    else:
        ans += r - l
        xo ^= A[l]
        l += 1
print(ans)
