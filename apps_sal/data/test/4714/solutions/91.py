(a, b) = map(int, input().split())
res = 0
for n in range(a, b + 1):
    s = str(n)
    if s == s[::-1]:
        res += 1
print(res)
