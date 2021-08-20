(s, x) = (input().lower(), int(input()))
print(''.join((ch.upper() if ord(ch) < x + 97 else ch.lower() for ch in s)))
