# A - Sandglass2
# https://atcoder.jp/contests/abc072/tasks/abc072_a

X, t = list(map(int, input().split()))

result = X - t

if result < 0:
    result = 0

print(result)

