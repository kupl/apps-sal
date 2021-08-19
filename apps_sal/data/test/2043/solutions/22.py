name = input()
s = input()
name_len = len(name)
l = -1
r = len(s)
index = 0
for ch in s:
    l += 1
    if ch == name[index]:
        index += 1
    if index == name_len:
        break
index = name_len - 1
for ch in s[::-1]:
    r -= 1
    if ch == name[index]:
        index -= 1
    if index == -1:
        break
if l < r:
    print(r - l)
else:
    print(0)
