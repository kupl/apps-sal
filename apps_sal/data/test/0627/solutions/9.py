n = int(input())
s = input()
p = -1
for i in range(n - 1):
    if ord(s[i]) > ord(s[i + 1]):
        p = i
        break
if p == -1:
    s = s[:-1]
else:
    s = s[:p] + s[p + 1:]
print(s)
