n = input()
s = input()
for i in range(len(s) - 1):
    if s[i + 1] < s[i]:
        print(s[:i] + s[i + 1:])
        return

print(s[:len(s) - 1])
