n = int(input())
s = input()
new_s = [0] * len(s)
ans = 0
for i in range(0, len(s), 2):
    if s[i] == s[i + 1]:
        ans += 1
        new_s[i] = s[i]
        new_s[i + 1] = 'b' if s[i] == 'a' else 'a'
    else:
        new_s[i] = s[i]
        new_s[i + 1] = s[i + 1]
print(ans)
print(''.join(new_s))
