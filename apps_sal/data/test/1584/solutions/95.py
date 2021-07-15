import bisect


def LI():
    return list(map(int, input().split()))


N = int(input())
L = LI()
L.sort()
ans = 0
for i in range(N-1, 1, -1):
    for j in range(i-1, 0, -1):
        ind = bisect.bisect_right(L, L[i]-L[j])
        if ind < j:
            ans += j-ind
print(ans)

