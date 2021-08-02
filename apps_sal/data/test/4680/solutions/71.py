"""
ABC042 A 和風いろはちゃんイージー
https://atcoder.jp/contests/abc042/tasks/abc042_a
"""

l = list(map(int, input().split()))
l5 = l.count(5)
l7 = l.count(7)

if l5 == 2 and l7 == 1:
    print("YES")
else:
    print("NO")
