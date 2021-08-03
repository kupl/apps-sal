'''
abc059 A - Three-letter acronym
https://atcoder.jp/contests/abc059/tasks/abc059_a
'''

s = list(input().split())
ans = ''
for i in s:
    ans += i[0].upper()
print(ans)
