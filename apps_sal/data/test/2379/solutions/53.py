
n, k, c = list(map(int, input().split()))
s = input()
l = [0] * k
r = [0] * k
p = 0
# for i in range(n):
i = 0
while i < n:
    if s[i] == "o":
        l[p] = i
        p += 1
        if (p >= k):
            break
        i += c
    i += 1
p = k - 1
# for i in range(n - 1, -1, -1):
i = n - 1
while i >= 0:
    if s[i] == "o":
        r[p] = i
        p -= 1
        if (p < 0):
            break
        i -= c
    i -= 1
#print(l, r)
for i in range(k):
    if l[i] == r[i]:
        print((l[i] + 1))
