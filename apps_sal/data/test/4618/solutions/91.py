s = input()
k = int(input())

SUBSTRINGS = set()
for i in range(len(s)):
    for j in range(i + 1, i + 6):
        SUBSTRINGS.add(s[i:j])

SUBSTRINGS = sorted(SUBSTRINGS)

print((SUBSTRINGS[k - 1]))

