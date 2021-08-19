(n, m) = list(map(int, input().split()))
s = str(input())
t = str(input())
a = n
b = 0
for i in range(0, m - n + 1):
    d = 0
    for j in range(0, n):
        if t[i + j] != s[j]:
            d = d + 1
    if d < a:
        a = d
        b = i
print(a)
for j in range(0, n):
    if t[b + j] != s[j]:
        print(j + 1)
