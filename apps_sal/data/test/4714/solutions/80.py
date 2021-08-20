(a, b) = map(int, input().split())
c = 0
for i in range(a, b + 1):
    s = str(i)
    if s == s[::-1]:
        c += 1
print(c)
