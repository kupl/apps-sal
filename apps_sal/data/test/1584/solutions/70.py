import bisect
N = int(input())
L = list(map(int, input().split()))

L = sorted(L)


# 二本を決める
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        # L[i] + L[j] より短い棒で且つjより大きいインデックスを数える
        ind = bisect.bisect_left(L, L[i] + L[j])
        num = ind - (j + 1)
        ans += max(num, 0)

print(ans)
