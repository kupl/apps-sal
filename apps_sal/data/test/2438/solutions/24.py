n = int(input())
s = input()
ans = n * (n + 1) / 2 - n
(count, i) = (0, 0)
l = list()
while i < n:
    c = s[i]
    val = 0
    while i < n and s[i] == c:
        i += 1
        val += 1
    l.append(val)
count += len(l) - 1
l = list(map(list, list(zip(l, l[1:]))))
for (a, b) in l:
    count += a - 1 + b - 1
print(int(ans - count))
