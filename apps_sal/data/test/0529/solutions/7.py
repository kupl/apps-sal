a, s = input().lower(), int(input())
print(''.join(t.upper() if ord(t) < s + 97 else t.lower() for t in a))
