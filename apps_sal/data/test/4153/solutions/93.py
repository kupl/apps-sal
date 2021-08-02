s = input()
r = 0
b = 0

for i in range(len(s)):
    if s[i] == "0":
        r += 1
    if s[i] == "1":
        b += 1

print(2 * min(r, b))
