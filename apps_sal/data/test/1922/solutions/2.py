'''
[C - Flip,Flip, and Flip......](https://atcoder.jp/contests/arc091/tasks/arc091_a)
'''

n, m = list(map(int, input().split()))

inner_num = (n - 2) * (m - 2)

ans = 0
if n == 1 and m == 1:
    ans = 1
elif n == 1:
    ans = m - 2
elif m == 1:
    ans = n - 2
else:
    outter_num = 0
    ans = inner_num

print(ans)
