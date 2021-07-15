from bisect import bisect_left


def can_make_tri(a, b, c):
    return a < b + c and b < c + a and c < a + b


N, *L = list(map(int, open(0).read().split()))
L.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        pos = bisect_left(L, L[i] + L[j], lo=j + 1)
        ans += pos - (j + 1)
print(ans)

