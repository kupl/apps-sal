s = input()

if s[0] == s[1]:
    print(1, 2)
    return

ans = [-1, -1]
for i in range(2, len(s)):
    if s[i] == s[i - 2]:
        ans = [i - 1, i + 1]
        break
    elif s[i] == s[i - 1]:
        ans = [i, i + 1]
        break
print(*ans)
