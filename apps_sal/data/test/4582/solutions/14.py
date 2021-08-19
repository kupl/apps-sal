"""
abc056 A - Honest Or Dishonest
https://atcoder.jp/contests/abc056/tasks/abc056_a
"""
(a, b) = input().split()
if a == 'H':
    if b == 'H':
        TopCoDeer = 'H'
    else:
        TopCoDeer = 'D'
elif b == 'H':
    TopCoDeer = 'D'
else:
    TopCoDeer = 'H'
print(TopCoDeer)
