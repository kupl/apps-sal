s = input()
k = int(input())
r = set()
for i in range(1, 6):
    for j in range(len(s) - i + 1):
        r.add(s[j:j + i])
l = list(r)
l = sorted(l)
print(l[k - 1])
