n = int(input())
s = input()
ans = 0
for c in s:
    if c == '+':
        ans += 1
    elif ans > 0:
        ans -= 1
print(ans)
