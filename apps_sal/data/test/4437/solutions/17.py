input()
s = input()

changes = 0
balance = 0
res = []

for i in range(len(s)):
    balance += 1 if s[i] == 'a' else -1
    res.append(s[i])

    if i % 2 == 1 and balance != 0:
        changes += 1
        res[-1] = chr(ord('a') + ord('b') - ord(res[-1]))
        balance = 0

print(changes)
print("".join(res))
