n = int(input())
s = input()

pre = ''
ans = 0
for c in s:
    if c != pre: ans += 1
    pre = c
print(ans)

