from bisect import bisect_left

N = int(input())
L = sorted(list(map(int, input().split())))
cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        tmp = bisect_left(L, L[i] + L[j])
        cnt += tmp - j - 1

print(cnt)
