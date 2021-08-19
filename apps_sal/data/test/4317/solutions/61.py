# A - +-x
# https://atcoder.jp/contests/abc137/tasks/abc137_a

a, b = list(map(int, input().split()))

result = [a + b, a - b, a * b]
print((max(result)))
