n = int(input())
S = input()
ans = ""
for s in S:
    if (ord(s) + n) > 90:
        ans += chr(64 + ((ord(s) + n) % 90))
    else:
        ans += chr(ord(s) + n)
print(ans)
