n = int(input())
s = input()
x = 1
for i in range(1, (n >> 1) + 1):
    if s[:i] == s[i:2 * i]:
        x = i
print(n - x + 1)

