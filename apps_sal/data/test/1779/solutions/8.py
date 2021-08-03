a1 = input()
a2 = input()
t = input()
mapping = dict()
for i in range(26):
    mapping[a1[i]] = a2[i]
    mapping[a1[i].upper()] = a2[i].upper()

ans = ""
for ch in t:
    if ch in mapping:
        ans += mapping[ch]
    else:
        ans += ch
print(ans)
