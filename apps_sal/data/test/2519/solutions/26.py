from itertools import accumulate
n, k = list(map(int, input().split()))
Pcum = [0] + list(accumulate(list(map(int, input().split()))))

ans = 0
for L in range(n):
    R = L + k
    if n < R:
        break
    cnt = (Pcum[R] - Pcum[L] + k) / 2
    if ans < cnt:
        ans = cnt
print(ans)
