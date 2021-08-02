n = int(input())
l = list(map(int, input().split()))
s = 1
m = 1
i = 1
while i <= n - 1:
    if l[i] > 2 * l[i - 1]:
        s = 1
    else:
        s += 1
    if s > m:
        m = s
    i += 1
print(m)
