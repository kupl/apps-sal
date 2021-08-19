n = int(input())
s = input()
num = 1
for i in range(1, n):
    if s[i] != s[i - 1]:
        num += 1
print(min(n, num + 2))
