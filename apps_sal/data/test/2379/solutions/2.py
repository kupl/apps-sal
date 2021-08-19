(n, k, c) = map(int, input().split())
s = list(input())
i = 0
l = [0] * k
r = [0] * k
j = 0
while i < n and l[-1] == 0:
    if s[i] == 'o':
        l[j] = i + 1
        i += c + 1
        j += 1
    else:
        i += 1
i = 0
j = k - 1
while i < n and r[0] == 0:
    if s[-i - 1] == 'o':
        r[j] = n - i
        i += c + 1
        j -= 1
    else:
        i += 1
for i in range(k):
    if r[i] == l[i]:
        print(r[i])
