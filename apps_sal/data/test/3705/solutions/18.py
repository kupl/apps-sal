n = int(input())
s = input()
c = 0
for i in range(0, len(s)):
    if s[i] == '8':
        c = c + 1
k = len(s) // 11
print(min(c, k))
