n = int(input())
s = input()
mask = 0
isunknown = [0] * n
for i in range(n):
    if s[i] != '*':
        mask |= 1 << ord(s[i]) - 97
    else:
        isunknown[i] = 1
m = int(input())
ans = (1 << 26) - 1
for i in range(m):
    words = input()
    umask = 0
    li = []
    for j in range(n):
        if isunknown[j]:
            umask |= 1 << ord(words[j]) - 97
            li.append('*')
        else:
            li.append(words[j])
    if umask & mask or s != ''.join(li):
        continue
    ans &= umask
realans = 0
while ans:
    realans += ans & 1
    ans >>= 1
print(realans)
