# A - Between Two Integers
# https://atcoder.jp/contests/abc061/tasks/abc061_a

A, B, C = list(map(int, input().split()))

result = 'No'

if A <= C <= B:
    result = 'Yes'

print(result)

