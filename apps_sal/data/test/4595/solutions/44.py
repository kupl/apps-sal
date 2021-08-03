s = list(input())
for i in range(len(s)):
    if s[i] == "A":
        start = i
        break
for j in reversed(range(0, len(s))):
    if s[j] == "Z":
        last = j
        break
print(last - start + 1)
