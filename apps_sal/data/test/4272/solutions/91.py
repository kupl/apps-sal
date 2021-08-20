n = int(input())
s = list(input())
b = 0
for a in range(n - 2):
    if s[a] == 'A' and s[a + 1] == 'B' and (s[a + 2] == 'C'):
        b = b + 1
print(b)
