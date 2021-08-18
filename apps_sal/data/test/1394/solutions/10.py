from sys import stdin

s = stdin.readline().strip()
b = ''.join([c for c in s if c != 'a'])
if len(b) % 2 == 1:
    print(":(")
elif b[:len(b) // 2] != b[len(b) // 2:]:
    print(":(")
elif 'a' in s[len(s) - len(b) // 2:]:
    print(":(")
else:
    print(s[:len(s) - len(b) // 2])
