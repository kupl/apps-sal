'''
abc060 A - Shiritori
https://atcoder.jp/contests/abc060/tasks/abc060_a
'''

s = list(input().split())
if s[0][-1] == s[1][0] and s[1][-1] == s[2][0]:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
