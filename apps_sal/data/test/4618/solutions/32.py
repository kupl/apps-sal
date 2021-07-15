s = input()
n = len(s)
k = int(input())
l = set()

for i in range(n):
    for j in range(1, 6):
        if i + j <= n:
            l.add(s[i: i + j])

l = sorted(l)
print((l[k - 1]))

