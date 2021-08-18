n, k, c = list(map(int, input().split()))
s = input()
l, r = [], []
i = 0
while i < n:
    if s[i] == "o":
        l.append(i)
        i += c + 1
    else:
        i += 1
i = n - 1
while i > -1:
    if s[i] == "o":
        r.append(i)
        i -= c + 1
    else:
        i -= 1
l = l[:k]
r = r[:k]
r = r[::-1]
for i in range(k):
    if l[i] == r[i]:
        print((l[i] + 1))
