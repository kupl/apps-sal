s = str(input())
ans = 0

for i in range(len(s) - 1, 0, -1):
    if i % 2 != 0:
        continue

    if s[0:i // 2] == s[i // 2:i] and i > ans:
        ans = i
    elif i <= ans:
        break

if len(s) == 2:
    ans = 2
print(ans)
