(a, b) = list(map(int, input().split()))
c = ''
d = ''
ans = 0
for i in range(a, b + 1):
    c = str(i)
    d = c[::-1]
    if c == d:
        ans += 1
print(ans)
