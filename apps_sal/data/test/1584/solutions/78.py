import bisect


def LI():
    return list(map(int, input().split()))


N = int(input())
L = LI()
L.sort()
ans = 0

for i in range(N-1, 1, -1):
    for j in range(i-1, 0, -1):
        xl = L[i]-L[j]
        ind = bisect.bisect_right(L, xl)
        if j > ind:
            ans += j-ind
print(ans)

