n, k = list(map(int, input().split()))
s = input()
d = [False] * 26
for c in s:
    d[ord(c) - ord('a')] = True
w = 0
l = 0
i = 0
while (i < 26) and (l < k):
    if d[i]:
        w += i + 1
        l += 1
        i += 2
    else:
        i += 1
if (l == k):
    print(w)
else:
    print(-1)
