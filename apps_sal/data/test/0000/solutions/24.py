s = input()
l = 0
end = 0
i = 1

while i <= len(s):
    if l == 0 and s[-i] == ']':
        l += 1
    elif l == 1 and s[-i] == ':':
        l += 1
        end = len(s) - i
        break
    i += 1

if l < 2:
    print(-1)
    return

for i in range(0, end):
    if l >= 4 and s[i] == '|':
        l += 1
    elif l == 2 and s[i] == '[':
        l += 1
    elif l == 3 and s[i] == ':':
        l += 1

if l >= 4:
    print(l)
else:
    print(-1)
