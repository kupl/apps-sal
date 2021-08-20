(n, k) = list(map(int, input().split(' ')))
s = input()
m = ''
if s[k - 1].isupper():
    m = s[k - 1].lower()
else:
    m = s[k - 1].upper()
print(s[:k - 1] + m + s[k:])
