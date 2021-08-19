def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
s = input().strip()
x = 0
while s[0] == s[x]:
    x += 1
y = 0
while s[-1] == s[n - 1 - y]:
    y += 1
if s[0] == s[-1]:
    ans = (x + 1) * (y + 1)
else:
    ans = x + y + 1
print(ans % 998244353)
