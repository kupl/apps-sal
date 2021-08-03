# A - Remaining Time
# https://atcoder.jp/contests/abc057/tasks/abc057_a

A, B = list(map(int, input().split()))

result = A + B
if result >= 24:
    result -= 24

print(result)
