"""
ABC045 A A - 台形
https://atcoder.jp/contests/abc045/tasks/abc045_a
"""

n = [int(input()) for i in range(3)]

print(((n[0] + n[1]) * n[2] // 2))
