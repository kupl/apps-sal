n, k, c = map(int, input().split())
s = input()
l = [0 for i in range(k)]
r = [0 for i in range(k)]
i, j = 0, 0
while i < n and (not l[-1]):
    if s[i] == "o":
        l[j] = i + 1
        i += c + 1
        j += 1
    else:
        i += 1
i, j = 0, k - 1
while i < n and (not r[0]):
    if s[n - i - 1] == "o":
        r[j] = n - i
        i += c + 1
        j -= 1
    else:
        i += 1
for i in range(k):
    if l[i] == r[i]:
        print(l[i])
