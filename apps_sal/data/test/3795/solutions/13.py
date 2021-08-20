n = int(input())
d = int(input())
e = int(input()) * 5
r = n
for i in range(d):
    if i * e > n:
        continue
    p = n - i * e - (n - i * e) // d * d
    r = min(r, p)
print(r)
