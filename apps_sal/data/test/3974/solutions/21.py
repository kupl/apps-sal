s = input()
ans = a1 = a2 = 0
for i in s:
    if i == '+':
        ans += 1
    else:
        ans -= 1
    a1 = max(a1, ans)
    a2 = min(a2, ans)
print(a1 + abs(a2))
