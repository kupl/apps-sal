from bisect import bisect_left
n = int(input())
L = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        (a, b) = (L[i], L[j])
        r = bisect_left(L, a + b)
        l = j + 1
        cnt += max(0, r - l)
print(cnt)
