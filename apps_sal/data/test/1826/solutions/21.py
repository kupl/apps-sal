n = int(input())
s = input()
a = 0
i = 0
while i < n - 1:
    if s[i] != s[i + 1]:
        i += 1
        a += 1
    i += 1
print(n - a)
