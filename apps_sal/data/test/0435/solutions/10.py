def read():
    return list(map(int, input().split()))


(n, k) = read()
s = input()
i = j = 0
cur = k
while cur and j < n:
    if s[j] == 'a':
        cur -= 1
    j += 1
while j < n and s[j] == 'b':
    j += 1
ans = j
while j < n:
    while i < n and s[i] == 'b':
        i += 1
    i += 1
    j += 1
    while j < n and s[j] == 'b':
        j += 1
    ans = max(ans, j - i)
i = j = 0
cur = k
while cur and j < n:
    if s[j] == 'b':
        cur -= 1
    j += 1
while j < n and s[j] == 'a':
    j += 1
ans = max(ans, j)
while j < n:
    while i < n and s[i] == 'a':
        i += 1
    i += 1
    j += 1
    while j < n and s[j] == 'a':
        j += 1
    ans = max(ans, j - i)
print(ans)
