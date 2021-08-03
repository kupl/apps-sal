n = int(input())
s = input()
ans = ""
i = 0
ad = 1
while i < n:
    ans += s[i]
    i += ad
    ad += 1
print(ans)
