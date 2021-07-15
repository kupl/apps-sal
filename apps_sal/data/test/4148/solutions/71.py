n = int(input())
s = list(input())
ans = ""
for char in s:
  ans += chr(((ord(char)-65 + n) % 26) + 65)

print(ans)
