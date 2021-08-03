n = int(input())
s = input()
res = n
for i in range(1, n // 2 + 1):
    if s[:i] == s[i:i * 2]:
        res = n - i + 1
print(res)
