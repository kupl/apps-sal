'''
abc057 A - Remaining Time
https://atcoder.jp/contests/abc057/tasks/abc057_a
'''

a, b = list(map(int, input().split()))
ans = (a + b) % 24
print(ans)
