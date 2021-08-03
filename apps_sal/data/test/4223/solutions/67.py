n = int(input())
s = input()
c = 1
for i in range(1, n):
    if s[i - 1] != s[i]:
        c += 1
print(c)
