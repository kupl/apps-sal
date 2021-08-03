"""
ABC047 A - キャンディーと2人の子供
https://atcoder.jp/contests/abc047/tasks/abc047_a
"""

l = list(map(int, input().split()))
l.sort()
if l[0] + l[1] == l[2]:
    print("Yes")
else:
    print("No")
