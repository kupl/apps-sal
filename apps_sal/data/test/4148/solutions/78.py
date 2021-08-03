n = int(input())
s = input()
ans = ''
for i in s:
    ans += chr((ord(i) + n - ord('A')) % 26 + ord('A'))
print(ans)
