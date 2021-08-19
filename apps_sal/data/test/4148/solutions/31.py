import string
N = int(input())
S = input()
a = string.ascii_uppercase
ans = ''
for s in S:
    ans += a[(a.index(s) + N) % len(a)]
print(ans)
