'''
abc061 A - Between Two Integers
https://atcoder.jp/contests/abc061/tasks/abc061_a
'''

i = list(map(int, input().split()))
if i[2] >= i[0] and i[1] >= i[2]:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
