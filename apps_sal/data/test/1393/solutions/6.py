x = input()
t = input()
d = dict()
for i in t:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
s = []
for i in x:
    s.append([i, 0])
s.sort(reverse=True)
ura = 0
opa = 0
for i in range(len(s)):
    if s[i][0] in d:
        if d[s[i][0]] > 0:
            ura += 1
            s[i][1] = 1
            d[s[i][0]] -= 1
for i in range(len(s)):
    if chr(ord(s[i][0]) - ord('a') + ord('A')) in d and s[i][1] == 0:
        if d[chr(ord(s[i][0]) - ord('a') + ord('A'))] > 0:
            opa += 1
            s[i][1] = 1
            d[chr(ord(s[i][0]) - ord('a') + ord('A'))] -= 1
for i in range(len(s)):
    if chr(ord(s[i][0]) - ord('A') + ord('a')) in d and s[i][1] == 0:
        if d[chr(ord(s[i][0]) - ord('A') + ord('a'))] > 0:
            opa += 1
            s[i][1] = 1
            d[chr(ord(s[i][0]) - ord('A') + ord('a'))] -= 1
print(ura, opa)
