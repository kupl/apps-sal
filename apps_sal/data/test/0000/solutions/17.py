s = input()
st = ""
idx = -1
for i in range(len(s)):
    if s[i] == '[':
        idx = i
        break
if idx == -1:
    print(-1)
    return
idxl = -1
for i in range(len(s) - 1, -1, -1):
    if s[i] == ']' and i > idx:
        idxl = i
        break
if idxl == -1:
    print(-1)
    return
col = col2 = -1
for i in range(len(s)):
    if s[i] == ':' and i > idx and i < idxl:
        col = i
        break
if col == -1:
    print(-1)
    return
for i in range(len(s) - 1, -1, -1):
    if s[i] == ':' and i > col and i < idxl:
        col2 = i
        break
if col2 == -1:
    print(-1)
    return
ans = 0
for i in range(col + 1, col2):
    if s[i] == '|':
        ans += 1
print(4 + ans)
