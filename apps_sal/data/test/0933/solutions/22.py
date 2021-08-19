s = input()
ans = ''
for i in s:
    if len(ans) >= 2 and i == ans[-1] and (i == ans[-2]):
        continue
    if len(ans) >= 3 and i == ans[-1] and (ans[-2] == ans[-3]):
        continue
    ans += i
print(ans)
