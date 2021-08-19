s = input()
k = int(input())
c = set()
for i in range(len(s)):
    for j in range(i + 1, i + 6):
        c.add(s[i:j])
print(sorted(list(c))[k - 1])
