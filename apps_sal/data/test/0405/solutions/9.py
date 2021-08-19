n = int(input())
s = input()
ans = 0
for c in s:
    if c == '<':
        ans += 1
    else:
        break
for c in reversed(s):
    if c == '>':
        ans += 1
    else:
        break
print(ans)
