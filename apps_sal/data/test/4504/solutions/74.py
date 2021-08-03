s = input()
n = len(s)
n -= 1
if n % 2:
    n -= 1
while n > 0:
    if s[:n // 2] == s[n // 2:n]:
        break
    n -= 2
print(n)
