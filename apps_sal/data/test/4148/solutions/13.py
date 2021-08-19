from string import ascii_uppercase
n = int(input())
s = input()
uu = ascii_uppercase * 3
d = {}
for i in range(27):
    d[uu[i]] = uu[i + n]
ans = ''
for c in s:
    ans += d[c]
print(ans)
