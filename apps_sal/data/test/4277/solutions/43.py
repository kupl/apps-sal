# A - T or T
# https://atcoder.jp/contests/abc133/tasks/abc133_a

N, A, B = list(map(int, input().split()))

result = N * A

if result >= B:
    result = B

print(result)
