n = int(input())
s = input()
total = 1
for c in 'RGB':
  total *= s.count(c)
for i in range(1, n - 1):
  for j in range(1, min(i + 1, n - i)):
    if s[i] != s[i - j] and s[i - j] != s[i + j] and s[i] != s[i + j]:
      total -= 1
print(total)
