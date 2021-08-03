s = str(input())
ans = 0
for moji in s:
    if moji == '+':
        ans += 1
    else:
        ans -= 1
print(ans)
