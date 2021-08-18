s = input()
n = len(s)
first, last = 0, 0

for i in range(n):
    b, f = i + 1, n - i
    if s[-1 - i] == 'A':
        first = f
    if s[i] == 'Z':
        last = b

print((last - first + 1))
