s = list(input())
for i in range(len(s)):
    if s[i] == "A":
        a = i
        break
for j in range(len(s) - 1, 0, -1):
    if s[j] == "Z":
        b = j
        break
print(b - a + 1)
