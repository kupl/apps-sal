"""
ABC067 A - Sharing Cookies
https://atcoder.jp/contests/abc067/tasks/abc067_a
"""
(a, b) = list(map(int, input().split()))
if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
    ans = 'Possible'
else:
    ans = 'Impossible'
print(ans)
