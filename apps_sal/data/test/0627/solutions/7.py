n = int(input())
s = input()

for i in range(n - 1):
    if ord(s[i]) > ord(s[i + 1]):
        print(s[:i] + s[i + 1:])
        return

print(s[:-1])

