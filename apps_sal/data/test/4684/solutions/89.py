'''
abc064 A - RGB Cards
https://atcoder.jp/contests/abc064/tasks/abc064_a
'''

r, g, b = list(map(int, input().split()))
i = r*100+g*10+b
if i%4 == 0:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)

