# A - RGB Cards
# https://atcoder.jp/contests/abc064/tasks/abc064_a

r, g, b = list(map(str, input().split()))

i = int(r + g + b)
result = 'NO'

if i % 4 == 0:
    result = 'YES'

print(result)

