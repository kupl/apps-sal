# https://atcoder.jp/contests/abc152/tasks/abc152_c

h, w = list(map(int, input().split()))

row = '#' * (w + 2)

print(row)
for _ in range(h):
    print(('#' + input() + '#'))

print(row)
