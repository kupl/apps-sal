n = int(input())
i = 1
l = 26
while l < n:
    i += 1
    l += 26**i
n -= l - 26**i + 1
s = ""
for k in range(i):
    s += chr(n % 26 + ord('a'))
    n //= 26
print(s[::-1])
