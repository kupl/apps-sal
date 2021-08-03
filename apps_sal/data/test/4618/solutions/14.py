s = input()
k = int(input())

subs = set()
for i in range(len(s)):
    for j in range(i + 1, min(i + 6, len(s) + 1)):
        sub = s[i:j]
        subs.add(sub)

print((sorted(list(subs))[k - 1]))
