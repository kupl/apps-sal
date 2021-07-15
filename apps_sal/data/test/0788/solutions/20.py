s = input()
ans = 0
for letter in s[1:] :
    x = int(letter)
    ans += x if x > 0 else 9
print(ans + 1)
