n = int(input())
s = input().split()[0]
res = 0
for i in range(len(s)):
    if s[i] == 'B':
        res += 2 ** i
print(res)
