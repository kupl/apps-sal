n, k = list(map(int, input().split()))
s = input()
N = [False] * 26
for i in range(n):
    N[ord(s[i]) - 97] = True
c = 0
w = 0
i = 0
while i < 26:
    if N[i]:
        c += 1
        w += i + 1
        i += 1
    i += 1
    if c == k:
        break
if c == k:
    print(w)
else:
    print(-1)
