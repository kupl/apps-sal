s = list(input())
n = len(s)

a = int((n - 1) / 2)
b = int((n + 3) / 2)

for i in range(a):
    if s[i] != s[n - 1 - i]:
        print("No")
        return

for i in range(a):
    if s[i] != s[a - 1 - i]:
        print("No")
        return

for i in range(a):
    if s[b + i - 1] != s[n - 1 - i]:
        print("No")
        return

print("Yes")
