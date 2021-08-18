import string

N = int(input())
S = input()

a = string.ascii_uppercase

ans = ''
for s in S:
    num = (a.index(s) + N) % len(a)
    ans += a[num]

print(ans)
