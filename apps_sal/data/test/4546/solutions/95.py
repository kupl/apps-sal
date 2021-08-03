'''
abc058 A - ι⊥l
https://atcoder.jp/contests/abc058/tasks/abc058_a
'''

a, b, c = list(map(int, input().split()))

if b - a == c - b:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
