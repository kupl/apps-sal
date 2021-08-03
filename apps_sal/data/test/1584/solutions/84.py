from bisect import bisect_left

N = int(input())

L = list(map(int, input().split()))
L.sort()

ans = 0


for i in range(N):
    for j in range(i + 1, N):
        c = L[i] + L[j]
        # a+bが入る場所を返す
        idx = bisect_left(L, c)
        ans += max(0, idx - (j + 1))

print(ans)
