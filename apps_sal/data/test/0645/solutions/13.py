import sys

s = input()

ans = 0
for c in s:
    if c in 'aeiou':
        ans += 1
    if c in '13579':
        ans += 1
print(ans)

