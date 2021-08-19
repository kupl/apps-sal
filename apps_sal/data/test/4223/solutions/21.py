n = int(input())
s = input()
c = 0
for i in range(n):
    if i == 0 or s[i] != s[i - 1]:
        c += 1
print(c)
