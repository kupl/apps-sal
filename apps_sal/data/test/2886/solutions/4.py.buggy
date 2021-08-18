from collections import Counter
s = input()
n = len(s)

for i in range(n):
    if n == 2:
        if s[0] == s[1]:
            print(1, 2)
            return
    if i == n - 2:
        break
    c = Counter(s[i:i + 3])
    v = c.most_common()
    if v[0][1] * 2 > len(s[i:i + 3]):
        print(i + 1, i + 3)
        return

print(-1, -1)
