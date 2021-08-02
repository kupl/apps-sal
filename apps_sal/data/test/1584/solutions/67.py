import bisect
n = int(input())
L = sorted(map(int, input().split()))
ans = 0

# 二分探索をするライブラリ

# c <= b <= a とする
# b < c + a と c < a + b　は自動で満たされる

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        a = L[n - 1 - i]
        b = L[n - 1 - j]

        c = a - b + 1
        # a < b + c を満たすｃの最小値

        if c <= b:
            ans += (n - 1 - j) - bisect.bisect_left(L, c)

print(ans)
