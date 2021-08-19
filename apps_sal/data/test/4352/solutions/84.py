"""
ABC054 - A one poker
https://atcoder.jp/contests/abc054/tasks/abc054_a
"""
(a, b) = list(map(int, input().split()))
if a == 1:
    a += 13
if b == 1:
    b += 13
if a > b:
    ans = 'Alice'
elif a < b:
    ans = 'Bob'
else:
    ans = 'Draw'
print(ans)
