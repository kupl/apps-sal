import string

N = int(input())
S = input()

# string.ascii_uppercase を覚えよう
a = string.ascii_uppercase
# a = ABCDEFGHIJKLMNOPQRSTUVWXYZ

ans = ''
for s in S:
    num = (a.index(s) + N) % len(a)
    ans += a[num]

print(ans)
