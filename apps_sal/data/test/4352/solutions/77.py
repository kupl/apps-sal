# A - One Card Poker
# https://atcoder.jp/contests/abc054/tasks/abc054_a

A, B = list(map(int, input().split()))

result = 'Alice'

if A == B:
    result = 'Draw'
elif A < B:
    if A == 1:
        result = 'Alice'
    else:
        result = 'Bob'
else:
    if B == 1:
        result = 'Bob'

print(result)
