# A - Favorite Sound
# https://atcoder.jp/contests/abc120/tasks/abc120_a

a, b, c = list(map(int, input().split()))

count = b // a

if count > c:
    count = c

print(count)

