# A - Good Integer
# https://atcoder.jp/contests/abc079/tasks/abc079_a

s = input()

if len(set(s[:3])) == 1 or len(set(s[1:])) == 1:
    print('Yes')
else:
    print('No')
