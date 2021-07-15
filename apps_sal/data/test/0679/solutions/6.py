s = input()

for i in range(1, len(s) - 1):
    if set(s[i - 1 : i + 2]) == set('ABC'):
        print("Yes")
        return

print("No")

