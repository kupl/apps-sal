s = input()
k = int(input())
c = set()
for i in range(len(s)):
    for j in range(k):
        c.add(s[i:i + j + 1])
print((sorted(list(c))[k - 1]))
