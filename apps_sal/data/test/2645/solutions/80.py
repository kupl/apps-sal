s = input()

ans = 0

for i in range(len(s)):
    if s[i] == 'g':
        ans += 1
    else:
        ans -= 1

print(ans // 2)
