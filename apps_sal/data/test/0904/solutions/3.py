import sys


def vol(i):
    ans = 0
    for j in i:
        if ('A' <= j <= 'Z'):
            ans += 1
    return ans


n = input()
gg = input().split()
ans = 0
for i in gg:
    ans = max(ans, vol(i))
print(ans)
