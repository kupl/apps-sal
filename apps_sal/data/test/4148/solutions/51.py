n = int(input())
s = input()
ans = ''
for letter in s:
    ans += chr(ord('A') +(ord(letter) - ord('A') + n) % 26)
print(ans)
