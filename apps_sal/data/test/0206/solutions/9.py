import math
M, A, B = map(int, input().split())
bound = [10**9 + 7]*(A + B)
l, r = 0, 0
while True:
    bound[l] = r
    if l >= B:
        l -= B
    else:
        l += A
    r = max(r, l)
    if l == 0:
        break

ans = 0
for i in range(0, A + B):
    if bound[i] <= M:
        ans += M - bound[i] + 1

rem = M - (A + B) + 1
if M >= (A + B):
    g = math.gcd(A, B)
    up = (rem // g) * g
    lo = rem - up
    cnt = up // g + 1
    ans += (lo + rem) * cnt // 2
print(ans)
