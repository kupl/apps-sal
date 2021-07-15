s = input()
ans = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == '1' or i == '3' or i == '5' or i == '7' or i == '9':
        ans += 1

print(ans)

