length = int(input())
s = input()

i = 0
j = -1
while s[i] == s[0]:
    i += 1

while s[j] == s[-1]:
    j -= 1

j += 1
j = int(abs(j))

if s[0] == s[-1]:
    print(((i + 1) * (j + 1)) % 998244353)
else:
    print((i + j + 1) % 998244353)
