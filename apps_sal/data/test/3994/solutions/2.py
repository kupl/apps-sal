3
n = int(input())
s = list(map(int, input()))
a = []
b = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    a.append(x)
    b.append(y)
mx = sum(s)
for i in range(1, 5000):
    for j in range(n):
        if i >= b[j] and (i - b[j]) % a[j] == 0:
            s[j] ^= 1
    mx = max(mx, sum(s))
print(mx)
