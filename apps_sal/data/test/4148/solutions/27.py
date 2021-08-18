n = int(input())
s = input()
ans = ""
for i in s:
    ans += chr(ord('A') + (ord(i) - ord('A') + n) % 26)
print(ans)
