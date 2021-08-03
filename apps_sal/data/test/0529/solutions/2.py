s, n = input(), int(input())

res = ''

for x in s.lower():
    if ord(x) < n + 97:
        res += x.upper()
    else:
        res += x

print(res)
