'''
abc056 A - Honest Or Dishonest
https://atcoder.jp/contests/abc056/tasks/abc056_a
'''

a, b = input().split()

if a == 'H':  # AtCoDeer正直
    if b == 'H':  # AtCoDeerくん「TopCoDeerくんは正直」
        TopCoDeer = 'H'
    else:
        TopCoDeer = 'D'
else:
    if b == 'H':
        TopCoDeer = 'D'
    else:
        TopCoDeer = 'H'
print(TopCoDeer)
