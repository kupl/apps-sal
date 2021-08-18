n, m, k = [int(i) for i in input().split()]
s = []
o = 0
for i in range(m):
    s.append([])
for i in range(n):
    l = [int(i) for i in input().split(" ")]
    for i in range(m):
        (s[i]).append(l[i])
result = 0
c = 0
for x in s:
    count = 0
    for i in range(n - k + 1):
        count = max(count, sum(x[i:i + k]))
        if count == k:
            break
    for i in range(n - k + 1):
        if sum(x[i:i + k]) == count:
            c += sum(x[:i])
            break
    result += count

print(result, c)
