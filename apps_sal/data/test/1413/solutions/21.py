n = int(input())
s = input()
a = 0
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        a += i + 1
print(a)
