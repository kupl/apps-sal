# A - abc of ABC
# https://atcoder.jp/contests/abc093/tasks/abc093_a

s = input()

if ''.join(sorted(s)) == 'abc':
    print('Yes')
else:
    print('No')
