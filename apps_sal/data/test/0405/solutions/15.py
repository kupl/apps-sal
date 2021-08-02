n = int(input())
p = 0;
s = input()
for i in range(len(s)):
    if s[i] == '<':
        p += 1;
    else:
        break;
for i in range(len(s) - 1, -1, -1):
    if s[i] == '>':
        p += 1;
    else:
        break;
print(p);
