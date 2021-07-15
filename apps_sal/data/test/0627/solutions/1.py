n = int(input())
s = input().strip()

for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        print(s[:i] + s[i+1:])
        return
print(s[:-1])

