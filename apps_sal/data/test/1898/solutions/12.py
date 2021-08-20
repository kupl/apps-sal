n = int(input())
s = ''
for i in range(n):
    s += 'I '
    s += ('love' if i % 2 else 'hate') + ' '
    if i + 1 < n:
        s += 'that '
    else:
        s += 'it'
print(s)
