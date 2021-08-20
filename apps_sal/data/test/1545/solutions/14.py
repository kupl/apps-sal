n = int(input())
s = input()
alf = list(map(int, input().split()))
d = [0 for i in range(n + 1)]
div = int(10 ** 9 + 7)
d[0] = 1
maxlen = -1
a = ord('a')
INF = int(10 ** 10)
md = [INF for i in range(n + 1)]
md[0] = 0
for i in range(1, n + 1):
    l = alf[ord(s[i - 1]) - a]
    minlen = l
    for j in range(l):
        if i - j < 1:
            break
        minlen = min(minlen, alf[ord(s[i - j - 1]) - a])
        if minlen < j + 1:
            break
        maxlen = max(maxlen, j + 1)
        d[i] += d[i - j - 1] % div
        d[i] %= div
        md[i] = min(md[i], 1 + md[i - j - 1])
print(d[n])
print(maxlen)
print(md[n])
