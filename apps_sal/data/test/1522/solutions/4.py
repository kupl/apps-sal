n = int(input())
s = input()
k = {}
ans = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in k:
            k[s[i]] = 1
        else:
            k[s[i]] += 1
    else:
        if s[i].lower() not in k or (s[i].lower() in k and k[s[i].lower()] <= 0):
            ans += 1
        else:
            k[s[i].lower()] -= 1
print(ans)
